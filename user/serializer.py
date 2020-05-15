
from rest_framework_jwt.settings import api_settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
from rest_framework import serializers
from django_redis import get_redis_connection
from user.models import User
import re

class UserModelSerializer(serializers.ModelSerializer):

    sms_code=serializers.CharField(max_length=20,write_only=True,label="验证码")

    #反序列化一个token字段返回前端
    token = serializers.CharField(read_only=True, label='jwt的字符串')
    class Meta:
        model=User
        '''
        attrs中的数据来源于fields字段中返回的
        '''
        fields =["id","username",'password','token',"sms_code",'email','mobile']
        extra_kwargs={
           "id":{
               "read_only":True
           },
            "username":{
                "read_only":True
            },
            "password":{
                "write_only":True
            },
            "email":{
                "read_only": True
            },
            'mobile':{
                "write_only": True
            }

        }

    def validate(self, attrs):
        mobile=attrs.get("mobile")
        password=attrs.get("password")
        sms_code=attrs.get("sms_code")

        print(mobile)
        print(sms_code)
        '''
        可以拿到具体的值（post参数传递过来）        
        print(mobile,"28")
        '''
        '''
            注意使用serializers.ValidationError()时，应抛异常，而不是用return
        '''


        '''
        验证手机号是否正确
        '''
        re_str=re.compile("^1[3|4|5|6|7|8|9]\d{9}")
        res=re_str.findall(mobile)
        if not res:
            raise serializers.ValidationError("手机号码不合法!")

        '''
        验证短信验证码
        '''
        try:
            redis=get_redis_connection("send_code")
        except:
            raise serializers.ValidationError("redis连接失败！")
        try:
            old_sms_code=redis.get("@%s"%mobile).decode()
            print(old_sms_code,'74')
        except:
            raise serializers.ValidationError("获取短信失败！")
        try:
            if old_sms_code != sms_code:
                raise serializers.ValidationError("验证码错误，请重新输入！")
        except:
            #用完之后将验证码删除
            redis.delete("@%s"%mobile)

        '''
        验证手机号是否注册
        '''
        try:
            User.objects.get(phone=mobile)
            raise serializers.ValidationError("手机号已存在")
        except:
            pass

        '''
        验证密码
        '''

        if len(password)<6 or len(password)>18:
            raise serializers.ValidationError("密码不符合要求，请重新输入！")





        '''
        attr参数传递给create方法中的validated_data(必须返回，否则alidated_data为None)
        '''
        return attrs



    def create(self, validated_data):
        password=validated_data.get("password")
        mobile=validated_data.get("mobile")
        print(mobile,'114')
        print(password,'115')
        '''
        attrs 传递给validated_data的值
        '''

        try:
            user = User.objects.create_user(
                mobile=mobile,
                username=mobile,
                password=password
            )
        except:
            raise serializers.ValidationError("注册用户失败，请联系客服工作人员！")

        '''
           手动签发jwt token串
        '''
        payload = jwt_payload_handler(user)
        user.token = jwt_encode_handler(payload)
        '''
        #并把模型数据返回回去
        '''
        return user



