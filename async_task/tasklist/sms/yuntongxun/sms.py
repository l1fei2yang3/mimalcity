from .CCPRestSDK import REST
# from django.conf import settings
from async_task.tasklist.sms import constent
#说明：主账号登录云通讯网站后， 可在“控制台-应用”中看到开发者主账号ACCOUNT SID
# _accountSid=settings.SMS_ACCOUNTSID
# _accountSid=settings.SMS_ACCOUNTSID
_accountSid=constent.SMS_ACCOUNTSID

#说明：主账号Token登录云通讯网站后， 可在“控制台-应用”中看到开发者主账号AUTH TOKEN
# _accountToken=settings.SMS_ACCOUNTOKEN
_accountToken=constent.SMS_ACCOUNTOKEN

#请使用管理控制台首页的APPID或自己创建的APPID
# appId=settings.SMS_APPID
appId=constent.SMS_APPID

#说明：请求地址生产环境配置 或app.cloopen.cpm
# _serverIP=settings.SMS_SERVERIP
_serverIP=constent.SMS_SERVERIP

#说明请求端口 生产环境为8883
_serverPort='8883'

#说明REST API版本号保持不变
_softVersion='2013-12-26'



class CCP(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(CCP,"_instance"):
            cls._instance=super(CCP,cls). __new__(cls, *args, **kwargs)
            cls._instance.rest=REST(_serverIP,_serverPort,_softVersion)
            cls._instance.rest.setAccount(_accountSid,_accountToken)
            cls._instance.rest.setAppId(appId)
        return cls._instance
    def send_template_sms(self,to,datas,temp_id):
        '''发送模板短信'''
        # to      手机号码
        #datas    内容数据，格式为数组，格式维数组，如果需要请填''
        #temp_id  模板id
        result=self.rest.sendTemplateSMS(to,datas,temp_id)
        print(result)
        #如果云通讯发送短信成功，返回的字段数据result中statusCode的值为"000000"
        if result.get("statusCode")=="000000":
            #返回0表示发送短信成功
            return 0
        else:
            # 返回-1表示发送短信失败
            return -1
if __name__ == '__main__':
    cpp=CCP()
    #注意测试短信模板为1【以后申请了可以有耕读ode模板】
    #参数1：客户端手机号码，测试时只能发给测试号码
    #参数2：短信模块中的数据
    #       短信验证码
    #       短信验证码有效期提示
    #参数3： 短信模板的ID开发测试时只能用1
    result=cpp.send_template_sms("18338663923",['1234',5],1)
    print(result)