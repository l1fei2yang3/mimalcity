from django.shortcuts import render

# Create your views here.




from rest_framework.generics import ListAPIView
from .serializer import BannerModelSerializer,MoblieListSerializer,MiddleNavHeaderSerializer

from .models import Banner,MoblieList,MiddleNavHeaderData,MiddleNavHeader
from .constent import BANNER_NUMBER,MENU_NUMBER,MIDNAV

class BannerAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_delete=False,is_show=True).order_by("-order")[:BANNER_NUMBER]
    serializer_class = BannerModelSerializer


class MoblieListAPIView(ListAPIView):
    queryset =MoblieList.objects.filter(is_delete=False,is_show=True)[:MENU_NUMBER]
    serializer_class = MoblieListSerializer


class MidlleNavAPIview(ListAPIView):
    queryset = MiddleNavHeader.objects.filter(is_delete=False,is_show=True)[:3]
    serializer_class = MiddleNavHeaderSerializer




