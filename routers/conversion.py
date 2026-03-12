from io import BytesIO 
from fastapi import APIRouter, Depends, HTTPException, Body
from fastapi.responses import StreamingResponse, FileResponse
from sqlalchemy.orm import Session
from pathlib import Path

from database import get_db
from schemas import MarkdownInput, ConversionResponse
from services import MarkdownService, ExcelService, DatabaseService
from config import settings
from models import MdExcelLog

router = APIRouter()
md_svc = MarkdownService()
excel_svc = ExcelService()
db_svc = DatabaseService()

@router.post("/md-to-excel/file")
def convert_to_file(
    data: MarkdownInput,
    db: Session = Depends(get_db)
):
    try:
        # 1. 解析
        df = md_svc.parse_to_dataframe(data.markdown)
        
        # 2. 保存文件 & 生成ID
        filepath = excel_svc.save_excel(df)
        batch_id = excel_svc.generate_batch_id()
        
        # 3. 写入数据库
        db_svc.save_conversion_records(db, filepath.name, batch_id, df, model_class=MdExcelLog)

        # 4. 返回流
        file_bytes = BytesIO(filepath.read_bytes())
        return StreamingResponse(
            file_bytes,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={"Content-Disposition": f"attachment; filename={filepath.name}"}
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # 生产环境建议使用 logger 记录详细堆栈
        raise HTTPException(status_code=500, detail=f"服务器内部错误: {str(e)}")

@router.post("/md-to-excel/path", response_model=ConversionResponse)
def convert_to_path(
    data: MarkdownInput,
    db: Session = Depends(get_db)
):
    try:
        df = md_svc.parse_to_dataframe(data.markdown)
        filepath = excel_svc.save_excel(df)
        batch_id = excel_svc.generate_batch_id()
        
        db_svc.save_conversion_records(db, filepath.name, batch_id, df, model_class=MdExcelLog)
        
        return ConversionResponse(
            success=True,
            file_path=str(filepath),
            download_url=f"/download/{filepath.name}",
            batch_id=batch_id
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/download/{filename}")
def download_file(filename: str):
    file_path = Path(settings.FILE_STORAGE_PATH) / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="文件不存在")
    return FileResponse(
        file_path,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=filename
    )