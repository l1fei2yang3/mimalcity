from django.urls import path



from .views import BannerAPIView,LeftMenuListAPIView,MidlleNavAPIview,TopAdsModelAPIView,MiddleAdsModelAPIView\
    ,LeftBottomAdsModelAPIView,RightBottomAdsModelAPIView

urlpatterns=[
    path("banner/",BannerAPIView.as_view()),
    path("menu/",LeftMenuListAPIView.as_view()),
    path("midnav/",MidlleNavAPIview.as_view()),
    path("tads/",TopAdsModelAPIView.as_view()),
    path("mads/",MiddleAdsModelAPIView.as_view()),
    path("lads/",LeftBottomAdsModelAPIView.as_view()),
    path("rads/",RightBottomAdsModelAPIView.as_view()),


]