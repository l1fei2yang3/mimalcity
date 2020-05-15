
from celery import Celery
#集成django(给该文件设置django环境)
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mimal.settings")
django.setup()

app=Celery("mimal")


#加载配置
app.config_from_object("async_task.config")

#加载任务
app.autodiscover_tasks(["async_task.tasklist.sms"])

#  celery -A mycelery.main worker --loglevel=info -P eventlet