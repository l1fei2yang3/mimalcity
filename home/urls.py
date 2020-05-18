from django.urls import path



from .views import BannerAPIView,MoblieListAPIView,MidlleNavAPIview

urlpatterns=[
    path("banner/",BannerAPIView.as_view()),
    path("menu/",MoblieListAPIView.as_view()),
    path("midnav/",MidlleNavAPIview.as_view()),
]