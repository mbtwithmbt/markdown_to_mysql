from sqlalchemy import Column, MetaData
from sqlalchemy.ext.declarative import declarative_base
from schemas_config import FIELD_MAPPING_CONFIG, SYSTEM_FIELDS_CONFIG, TABLE_NAME

Base = declarative_base()

def create_dynamic_model(table_name: str, field_config: dict, system_fields: list):
    """
    动态创建 SQLAlchemy ORM 模型
    """
    # 动态生成类属性字典
    attrs = {
        "__tablename__": table_name,
        "__table_args__": {"extend_existing": True, "mysql_charset": "utf8mb4"}
    }

    # 1. 添加系统字段
    for field in system_fields:
        col_args = {
            "primary_key": field.get("primary_key", False),
            "autoincrement": field.get("autoincrement", False),
            "nullable": field.get("nullable", True),
            "index": field.get("index", False),
        }
        # 处理默认值
        if "default" in field:
            val = field["default"]
            
            # 如果是 callable (如 datetime.now)，说明是 Python 端默认值
            if callable(val):
                col_args["default"] = val
            # 如果是静态值 (如 "success")，我们可以同时设置 Python 默认值和数据库默认值
            else:
                col_args["default"] = val
                col_args["server_default"] = str(val)
            
        attrs[field["db_column"]] = Column(field["type"], **col_args)

    # 2. 添加业务字段（根据配置循环生成）
    for md_header, config in field_config.items():
        attrs[config["db_column"]] = Column(
            config["type"],
            nullable=True, # 业务字段通常允许为空
            comment=config.get("comment", "")
        )

    # 动态创建类
    return type("MdExcelLog", (Base,), attrs)

# 生成最终的模型类
MdExcelLog = create_dynamic_model(TABLE_NAME, FIELD_MAPPING_CONFIG, SYSTEM_FIELDS_CONFIG)