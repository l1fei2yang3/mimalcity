
from rest_framework import serializers

from .constent import MID_NAVDATA
from .models import Banner,MoblieList,MiddleNavHeaderMobile,MiddleNavHeader
class BannerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Banner
        fields=["id","banner_url"]


class MoblieListSerializer(serializers.ModelSerializer):
    class Meta:
        model=MoblieList
        fields=["id","banner_url","name"]







'''
:param 序列化（过滤序列化器）
'''
'''
:param 从表数据进行过滤
'''

class FilterdListSerializer(serializers.ListSerializer):
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
        return super().to_representation(data)


'''
:param 从表
'''
class MiddleNavHeaderDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=MiddleNavHeaderMobile
        fields=["title"]

        '''
        将从表数据进行过滤
        '''
        list_serializer_class = FilterdListSerializer

'''
:param 通过主表获得从表
'''
class MiddleNavHeaderSerializer(serializers.ModelSerializer):
    '''
    :param 序列化从表

    '''

    mid_data=MiddleNavHeaderDataSerializer(many=True)

    class Meta:
        model=MiddleNavHeader
        fields=["id","title","mid_data"]