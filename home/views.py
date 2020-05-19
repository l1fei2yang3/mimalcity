
from django.shortcuts import render

# Create your views here.




from rest_framework.generics import ListAPIView
# from .serializer import BannerModelSerializer,MoblieListSerializer,MiddleNavHeaderSerializer,TopAdsModelSerializer
from rest_framework.views import APIView



from rest_framework.response import Response

from . import serializer
from .models import Banner,MoblieList,MiddleNavHeader,AdsList,MiddleAdsList,LeftBottomAdsList,RightBottomAdsList,LeftMenu
from .constent import BANNER_NUMBER, MENU_NUMBER, MID_NAV,TOP_ADS,MIDDLE_ADS,LEFT_BOTTOM_ADS,RIGHT_BOTTOM_ADS,LEFT_MENU_NUMBER


class BannerAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_delete=False,is_show=True).order_by("-order")[:BANNER_NUMBER]
    serializer_class = serializer.BannerModelSerializer





class LeftMenuListAPIView(APIView):

    def get(self,request,*args,**kwargs):
        data=LeftMenu.objects.filter(is_delete=False, is_show=True)[:LEFT_MENU_NUMBER]
        ret=serializer.LeftMenuListSerializer(data,many=True)

        for i in ret.data:
            if i["lmenu"]:
                c=[]
                for j in range(4,25,4):
                    c.append(i["lmenu"][j-4:j])
                i["lmenu"]=c
            else:
                i["lmenu"]=None


        return Response(ret.data)



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
    serializer_class = serializer.MiddleNavHeaderSerializer


class TopAdsModelAPIView(ListAPIView):
    queryset = AdsList.objects.filter(is_show=True,is_delete=False)[:TOP_ADS]
    serializer_class = serializer.TopAdsModelSerializer



class MiddleAdsModelAPIView(ListAPIView):
    queryset = MiddleAdsList.objects.filter(is_show=True,is_delete=False)[:MIDDLE_ADS]
    serializer_class = serializer.MiddleModelSerializer

class LeftBottomAdsModelAPIView(ListAPIView):
    queryset = LeftBottomAdsList.objects.filter(is_show=True,is_delete=False)[:LEFT_BOTTOM_ADS]
    serializer_class = serializer.LeftBottomModelSerializer



class RightBottomAdsModelAPIView(APIView):
    def get(self,request,*args,**kwargs):
        brm=RightBottomAdsList.objects.filter(is_show=True,is_delete=False)[:8]
        # {"id": brm[count].id, "images_url": brm[count].images_url,
        #  "title": brm[count].title, "desc": brm[count].discrable,
        #  "is_new": brm[count].is_new, "color": brm[count].color,
        #  # "price": brm[count].price}
        # #

        res=serializer.RightBottomModelSerializer(brm,many=True)



        '''
        
        :param 不能写在序列化器当中，SerializerMethodField定义的方法函数会重复多次调用  
        '''
        data=[]
        for i in range(4,9,4):
            data.append(res.data[i-4:i])

        return Response(data)
