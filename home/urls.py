from django.urls import path



from .views import BannerAPIView,MoblieListAPIView

urlpatterns=[
    path("banner/",BannerAPIView.as_view()),
    path("menu/",MoblieListAPIView.as_view()),
]