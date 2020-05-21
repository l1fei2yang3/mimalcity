"""
Django settings for mimal project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h1h29(82jm)1wt_ovi!z7t3c#ec4_r_bnzu&c6786+p2zq7+se'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["api.mimal.cn",]


# Application definition

INSTALLED_APPS = [

    #主题应放在最上面
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    # 解决跨域问题
    'corsheaders',
    'user',
    'home',

    'product'

]

MIDDLEWARE = [
     #设置corsheaders中间件(用于跨域)
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mimal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mimal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "mimal",
        "USER":"root",
        "PASSWORD":"123456",
        "HOST":"127.0.0.1",
        "PORT":3306
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT=os.path.join(BASE_DIR,"media")
STATICFILES_DIRS=[os.path.join(BASE_DIR,"static"),MEDIA_ROOT]

# CORS_ORIGIN_WHITELIST=(
#     'http://www.mimal.cn:8080/',
# )
#允许ajax跨域请求时携带cookie(需要前后端同时打开)

CORS_ALLOW_CREDENTIALS = True


CORS_ORIGIN_ALLOW_ALL = True





#继承了django.contrib.auth.model下AbstractUser，故必须写它
AUTH_USER_MODEL="user.User"



#设置jwt

REST_FRAMEWORK = {

#修改优先使用的身份(登录)认证方式
    'DEFAULT_AUTHENTICATION_CLASSES': (
        #选择使用jsonwebtoken认证
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        #检查CSRF认证
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),

}


#jwt字符串有效期
import datetime
JWT_AUTH = {
    #jwt字符串有效期
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    # 认证处理类（主要用于返回多个值，而不是只返回Token字符串）
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'user.utils.jwt_response_payload_handler',

}


'''
配置缓存
'''

CACHES = {
    #默认缓存
    "default":{
        "BACKEND":"django_redis.cache.RedisCache",
        #存放位置
        "LOCATION":"redis://127.0.0.1:6379/6",
        "OPTIONS":{
            "CLIENT_CLASS":"django_redis.client.DefaultClient",
        }
    },

    # '''默认session'''
    # "session":{
    #     "BACKEND":"django_redis.cache.RedisCache",
    #     '''存放位置'''
    #     "LOCATION":"redis://127.0.0.1:6379/7",
    #     "OPTIONS":{
    #         "CLIENT_CLASS":"django_redis.client.DefaultClient",
    #     }
    # },
    #默认发送短信验证
    "send_code":{
            "BACKEND":"django_redis.cache.RedisCache",
            #存放位置
            "LOCATION":"redis://127.0.0.1:6379/9",
            #客户端选项
            "OPTIONS":{
                "CLIENT_CLASS":"django_redis.client.DefaultClient",
        }
    }

}
# CACHES = {
#     # 默认缓存
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         # 项目上线时,需要调整这里的路径
#         #放入0号数据库
#         "LOCATION": "redis://127.0.0.1:6379/6",
#         #配置客户端为默认客户端
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     },
#     # 提供给xadmin或者admin的session存储
#     "session": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/7",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     },
#     # 提供存储短信验证码
#     "sms_code":{
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/9",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     },
#     # "cart":{
#     #     "BACKEND": "django_redis.cache.RedisCache",
#     #     "LOCATION": "redis://127.0.0.1:6379/3",
#     #     "OPTIONS": {
#     #         "CLIENT_CLASS": "django_redis.client.DefaultClient",
#     #     }
#     # },
# }

#容联云手机号注册
SMS_ACCOUNTSID='8aaf0708701ea9ab01702d750d05046a'
SMS_ACCOUNTOKEN='fa3baccd084144dd8e20050270463bdc'
SMS_APPID="8aaf0708701ea9ab01702d750d5b0470"
SMS_SERVERIP="sandboxapp.cloopen.com"