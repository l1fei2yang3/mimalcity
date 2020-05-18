
from django.shortcuts import render

# Create your views here.




from rest_framework.generics import ListAPIView
from .serializer import BannerModelSerializer,MoblieListSerializer,MiddleNavHeaderSerializer

from .models import Banner,MoblieList,MiddleNavHeaderMobile,MiddleNavHeader
from .constent import BANNER_NUMBER, MENU_NUMBER, MID_NAV


class BannerAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_delete=False,is_show=True).order_by("-order")[:BANNER_NUMBER]
    serializer_class = BannerModelSerializer


class MoblieListAPIView(ListAPIView):
    queryset =MoblieList.objects.filter(is_delete=False,is_show=True)[:MENU_NUMBER]
    serializer_class = MoblieListSerializer





class MidlleNavAPIview(ListAPIView):
    '''
    # from django.db.models import Subquery,OuterRef #子查询
    :param OuterRef Subquery子查询
    from django.db.models import Prefetch（与prefetch_related搭配使用）
    :param prefetch_related：查询关联的每张表，可以链式调用
    :param select_related：连接查询（效率比prefetch_related高），可以链式调用
    queryset = MiddleNavHeader.objects.filter(is_delete=False,is_show=True)[:MID_NAV].prefetch_related(
    #Prefetch预查询机制：因此不能进行限制查询
    Prefetch('mid_data', queryset=MiddleNavHeaderData.objects.filter(is_delete=False,is_show=True)[:3],to_attr="example_posts"
    #报错
    ))
    '''
    queryset = MiddleNavHeader.objects.filter(is_delete=False, is_show=True)[:MID_NAV]
    serializer_class = MiddleNavHeaderSerializer




