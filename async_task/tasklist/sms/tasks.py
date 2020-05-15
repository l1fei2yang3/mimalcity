#celery的任务必须写在tasks.py的文件中，别的名称不识别
from async_task.main import app

from async_task.tasklist.sms.yuntongxun.sms import CCP
from async_task.tasklist.sms.constent import SMS_EXPIRE_TIME,SMS_TEMPLATE_ID
import logging
log=logging.getLogger('django')
#h创建任务，如果不填默认使用函数名
@app.task(name='sending_sms')
def sending_sms(mobile,code):
    ccp=CCP()
    result=ccp.send_template_sms(mobile, [code, SMS_EXPIRE_TIME // 60], SMS_TEMPLATE_ID)
    if result == -1:
        # 发送失败
        log.error("发送短信失败！手机号:%s" % mobile)
    else:
        return "发送短信成功！"