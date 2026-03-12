Markdown_to_excel/
├── .env                # 环境变量配置（数据库密码等敏感信息）
├── requirements.txt    # 依赖包
├── main.py             # 入口文件
├── config.py           # 配置管理
├── database.py         # 数据库连接管理
├── models.py           # 数据库表模型 (ORM)
├── schemas.py          # 数据校验模型
├── services.py         # 核心业务逻辑 (Markdown解析、Excel生成、DB写入)
└── routers/
    └── conversion.py   # API 路由接口

    