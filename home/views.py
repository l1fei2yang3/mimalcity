from django.shortcuts import render

# Create your views here.




from rest_framework.generics import ListAPIView
from .serializer import BannerModelSerializer,MoblieListSerializer

from .models import Banner,MoblieList
from .constent import BANNER_NUMBER,MENU_NUMBER

class BannerAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_delete=False,is_show=True).order_by("-order")[:BANNER_NUMBER]
    serializer_class = BannerModelSerializer


class MoblieListAPIView(ListAPIView):
    queryset =MoblieList.objects.filter(is_delete=False,is_show=True)[:MENU_NUMBER]
    serializer_class =MoblieListSerializer


