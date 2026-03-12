from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings
from models import Base # 导入动态生成的 Base

# 创建数据库引擎
engine = create_engine(
    settings.DATABASE_URL, 
    pool_pre_ping=True, # 自动检测连接是否有效
    pool_recycle=3600   # 连接回收时间
)

# 在 main.py 启动时调用 init_db()
def init_db():
    """
    初始化数据库（建表）
    """
    # 这里的 Base 包含了动态生成的所有字段定义
    Base.metadata.create_all(bind=engine)


# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 依赖注入：获取数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ... 原有内容 ...


