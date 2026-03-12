## 项目结构
Markdown_to_excel/
├── .env                # 环境变量配置（数据库密码等敏感信息）
├── pyproject.toml    # 依赖包
├── main.py             # 入口文件
├── config.py           # 配置管理
├── database.py         # 数据库连接管理
├── models.py           # 数据库表模型 (ORM)
├── schemas.py          # 数据校验模型
├── services.py         # 核心业务逻辑 (Markdown解析、Excel生成、DB写入)
└── routers/
    └── conversion.py   # API 路由接口

## 环境配置
### python环境同步
```bash
uv sync
```

## 项目配置
### 数据库连接配置（mysql）
.env
文件样例
```
DB_HOST=192.168.31.195
DB_PORT=3306
DB_USER=user
DB_PASSWORD=password
DB_DATABASE=test
```

### 表字段映射配置
schemas_config.py
启动项目自动检测是否存在目标表，如果不存在则创建

### 启动端口配置兼入口函数
main.py

### 接口文档
base_url:port/docs

## 启动项目
uv run main.py