"""
celery配置文件
注意命名规范，大写（允许其他访问）
"""

BROKER_URL = "redis://127.0.0.1:6379/2"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/3"