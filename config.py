import os

class Config:
    # 飞书应用配置
    FEISHU_APP_ID = os.environ.get("FEISHU_APP_ID")
    FEISHU_APP_SECRET = os.environ.get("FEISHU_APP_SECRET")
    
    # 多维表格配置
    BASE_ID = os.environ.get("BASE_ID")
    TABLE_ID = os.environ.get("TABLE_ID")
    
    # Flask Secret Key (也应该来自环境变量)
    SECRET_KEY = os.environ.get('SECRET_KEY', 'a-default-fallback-secret-key-if-not-set')