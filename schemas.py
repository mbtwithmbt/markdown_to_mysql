from pydantic import BaseModel
from typing import Optional

class MarkdownInput(BaseModel):
    markdown: str

class ConversionResponse(BaseModel):
    success: bool
    file_path: Optional[str] = None
    download_url: Optional[str] = None
    batch_id: str
    detail: Optional[str] = None