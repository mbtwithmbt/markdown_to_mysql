import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

class Settings:
    # 数据库配置
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", 3306))
    DB_USER: str = os.getenv("DB_USER", "root")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DB_DATABASE: str = os.getenv("DB_DATABASE", "test")
    
    # 文件存储路径
    FILE_STORAGE_PATH: str = "files"

    @property
    def DATABASE_URL(self):
        # SQLAlchemy 连接字符串格式
        return f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_DATABASE}"

settings = Settings()   