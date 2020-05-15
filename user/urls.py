from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserAPIView,SMSAPIView,CheckMobileAPIview,CheckUserNameAPIview,LoginUserAPIView
# routers=DefaultRouter()
# routers.register('regist',UserAPIView)
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns=[
    # path('',include(routers.urls))

    #要想使用应先注册超级用户 python manage.py createsuperuser  (或者注册成功后才会放回ttoken值)
    path("login/",obtain_jwt_token),
    path('send_ems/',SMSAPIView.as_view()),
    path("check_mobile/",CheckMobileAPIview.as_view()),
    path("regist/",UserAPIView.as_view()),
    path("check_username/",CheckUserNameAPIview.as_view()),
    # path("login/",LoginUserAPIView.as_view()),

]