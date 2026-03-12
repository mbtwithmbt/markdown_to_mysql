from sqlalchemy import String, Text, Integer, DateTime
from datetime import datetime

# ======================
# 字段映射配置
# ======================
# key: Markdown 表头名称
# value: 数据库配置字典
FIELD_MAPPING_CONFIG = {
    # 业务字段
    "一级类别": {"db_column": "level1_category", "type": String(255), "comment": "一级类别"},
    "二级类别": {"db_column": "level2_category", "type": String(255), "comment": "二级类别"},
    "审计工单事项": {"db_column": "audit_item", "type": Text, "comment": "审计工单事项"},
    "法规名称": {"db_column": "regulation_name", "type": String(255), "comment": "法规名称"},
    "法规条例": {"db_column": "regulation_article", "type": String(255), "comment": "法规条例"},
    "审计措施": {"db_column": "audit_measure", "type": Text, "comment": "审计措施"},
    "限制内容摘要": {"db_column": "restriction_summary", "type": Text, "comment": "限制内容摘要"},
    "使用范围说明": {"db_column": "usage_scope", "type": Text, "comment": "使用范围说明"},
}

# 表名配置
TABLE_NAME = "md_excel_logs"

# 系统默认字段（不需要从 Markdown 解析，由程序自动生成）
SYSTEM_FIELDS_CONFIG = [
    {"db_column": "id", "type": Integer, "primary_key": True, "autoincrement": True},
    {"db_column": "filename", "type": String(255), "nullable": False},
    {"db_column": "batch_id", "type": String(50), "nullable": False, "index": True},
    {"db_column": "created_at", "type": DateTime, "default": datetime.now},
    {"db_column": "status", "type": String(20), "default": "success"},
]