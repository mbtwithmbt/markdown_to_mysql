from contextlib import asynccontextmanager
from fastapi import FastAPI
from routers import conversion
from database import init_db

# 1. 定义 lifespan 上下文管理器
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup 逻辑：应用启动时执行
    print("应用启动中... 正在初始化数据库表结构")
    init_db()
    yield
    # Shutdown 逻辑：应用关闭时执行 (如果需要清理资源，可以写在这里)
    print("应用已关闭")

# 2. 将 lifespan 传递给 FastAPI 应用
app = FastAPI(
    title="Markdown 转 Excel 接口 (动态配置版)",
    lifespan=lifespan  # <--- 关键修改点
)

# 引入路由
app.include_router(conversion.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5175, reload=True)