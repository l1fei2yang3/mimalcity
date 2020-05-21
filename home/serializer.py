
from rest_framework import serializers

from .constent import MID_NAVDATA,MENU_NUMBER
from .models import Banner,MoblieList,MiddleNavHeaderMobile,MiddleNavHeader,AdsList,\
    MiddleAdsList,LeftBottomAdsList,RightBottomAdsList,LeftMenu




'''
轮播图产品位
'''
class BannerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Banner
        fields=["id","banner_url","product_id"]



'''
手机菜单产品位
'''



'''
:param 过滤表

'''
class FilterMenuSerializer(serializers.ListSerializer):
    '''
    :param 重写to_representation方法
    '''
    
    def to_representation(self, data):
        '''


        :param data: 模型对象  home.MiddleNavHeaderData.None
        :return:
        '''
        # filter替换末尾None
        data=data.filter(is_show=True,is_delete=False)[:MENU_NUMBER]

        '''
            需返回结果
        '''
        return super(FilterMenuSerializer, self).to_representation(data)
'''
:param 从表
'''
class MobileListMenu(serializers.ModelSerializer):
    class Meta:
        model=MoblieList
        fields=["name",'banner_url','id',"product_id"]
        list_serializer_class = FilterMenuSerializer

'''
:param 主表
'''
class LeftMenuListSerializer(serializers.ModelSerializer):
    lmenu=MobileListMenu(many=True)
    class Meta:
        model=LeftMenu
        fields=["id","title","lmenu"]





'''


  中部导航栏产品位

'''



'''
:param 从表数据进行过滤
:param 序列化（过滤序列化器）
'''
class FilterListSerializer(serializers.ListSerializer):
    '''
    :param 重写to_representation方法
    '''
    def to_representation(self, data):
        '''


        :param data: 模型对象  home.MiddleNavHeaderData.None
        :return:
        '''
        # filter替换末尾None
        data=data.filter(is_show=True,is_delete=False)[:MID_NAVDATA]
        
        '''
        需返回结果
        '''
        return super(FilterListSerializer, self).to_representation(data)


'''
:param 从表
'''
class MiddleNavHeaderDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=MiddleNavHeaderMobile
        fields=["title","images_url","price",'id',"product_id"]
        '''
        将从表数据进行过滤
        '''
        list_serializer_class = FilterListSerializer

'''
:param 通过主表获得从表
'''
class MiddleNavHeaderSerializer(serializers.ModelSerializer):
    '''
    :param 序列化从表

    '''

    mid_header=MiddleNavHeaderDataSerializer(many=True)

    class Meta:
        model=MiddleNavHeader
        fields=["id","title","mid_header"]




'''
:param 上产品位

'''

class TopAdsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdsList
        fields = ["id","images_url","product_id"]


'''
:param 中部产品位
'''
class MiddleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=MiddleAdsList
        fields = ["id", "images_url","product_id"]


'''
左下产品位
'''

class LeftBottomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=LeftBottomAdsList
        fields = ["id", "images_url","product_id"]



'''
右下产品位
'''
class RightBottomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=RightBottomAdsList
        fields=["id","images_url","discrable","price","title","color","is_new","product_id"]








