from sqlalchemy import String, Text, Integer, DateTime
from datetime import datetime

# ======================
# 字段映射配置
# ======================
# key: Markdown 表头名称
# value: 数据库配置字典
FIELD_MAPPING_CONFIG = {
    # 业务字段
    "序号": {"db_column": "序号", "type": String(50), "comment": "序号"},
    "一级审计事项": {"db_column": "一级审计事项", "type": String(255), "comment": "一级审计事项"},
    "二级审计事项": {"db_column": "二级审计事项", "type": String(255), "comment": "二级审计事项"},
    "三级审计事项": {"db_column": "三级审计事项", "type": Text, "comment": "三级审计事项"},
    "法规名称": {"db_column": "法规名称", "type": String(255), "comment": "法规名称"},
    "法规条例": {"db_column": "法规条例", "type": Text, "comment": "法规条例"},
    "审计措施": {"db_column": "审计措施", "type": Text, "comment": "审计措施"},
    "适用主体": {"db_column": "适用主体", "type": Text, "comment": "适用主体"},
    "适用范围": {"db_column": "适用范围", "type": Text, "comment": "适用范围"},
}

# 表名配置
TABLE_NAME = "宁波总工会审计工单"

# 系统默认字段（不需要从 Markdown 解析，由程序自动生成）
SYSTEM_FIELDS_CONFIG = [
    {"db_column": "id", "type": Integer, "primary_key": True, "autoincrement": True},
    {"db_column": "filename", "type": String(255), "nullable": False},
    {"db_column": "batch_id", "type": String(50), "nullable": False, "index": True},
    {"db_column": "created_at", "type": DateTime, "default": datetime.now},
    {"db_column": "status", "type": String(20), "default": "success"},
]