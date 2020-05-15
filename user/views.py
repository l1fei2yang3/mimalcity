from .models import User
from .serializer import UserModelSerializer

from rest_framework.generics import CreateAPIView,GenericAPIView,ListAPIView
from async_task.tasklist.sms.tasks import sending_sms
from rest_framework.response import Response
from .constant import SMS_INTERVAL_TIME
from django_redis import get_redis_connection
from rest_framework.views import APIView
import random,string


from rest_framework import status


'''
发送短信
'''
class SMSAPIView(APIView):

    def get(self,request,*args,**kwargs):
        mobile=request.query_params.get("mobile")
        print(mobile)
        try:
            User.objects.get(phone=mobile)
            return Response({"res":"手机号已存在！"})
        except:
            pass
        code="".join(random.sample(string.digits,6))
        try:
            print("******31********")


            '''
            send_code：获取在settings文件当中配置的缓存
            '''
            #send_code redis连接别名
            redis=get_redis_connection("send_code")
            print("******33********")
            #查看
            is_alive=redis.get("mobile_"+mobile)
            if is_alive:
                return Response({"result":"对不起，短信间隔不超过一秒"},status=status.HTTP_304_NOT_MODIFIED)

            pip=redis.pipeline()
            pip.multi()
            print("******40********")
            #设置短信间隔时间
            pip.setex("mobile_"+mobile,SMS_INTERVAL_TIME,"timer")
            print("******50********")

            #保存手机号及验证码
            pip.setex("@%s"%mobile,SMS_INTERVAL_TIME,code)
            print("******55********")
            pip.execute()
            print("******50********")
            #异步发送短信(celery)
            sending_sms.delay(mobile,code)
        except:
            return Response({"result":"验证码发送失败！"},status=status.HTTP_304_NOT_MODIFIED)
        return Response({"result":"验证码发送成功！"},status=status.HTTP_200_OK)




'''
验证手机号码是否注册
'''

class CheckMobileAPIview(APIView):
    def get(self,request,*args,**kwargs):
        mobile=request.query_params.get("mobile")
        print(mobile)
        try:
            User.objects.get(mobile=mobile)
            return Response({"res":"账号已存在，请重新输入！"},status=status.HTTP_304_NOT_MODIFIED)
        except:
            return Response({"res":'ok'})





#CreateAPIView：默认只封装POST方法     ListAPIView:默认只封装了GET方法
class UserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer




class CheckUserNameAPIview(APIView):
    def get(self,request,*args,**kwargs):
        username=request.query_params.get("username")
        print(username,'95')
        user=User.objects.filter(username=username)
        if user:
            return Response("账号可以登录!")
        return Response("没有此账号，请进行注册!")


class LoginUserAPIView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        username=request.data.get("username")
        password=request.data.get("password")
        user=User.objects.filter(username=username,password=password)
        if user:
            return Response({"res":"ok"},status=status.HTTP_200_OK)
        return Response({"res":"no"},status=status.HTTP_404_NOT_FOUND)


