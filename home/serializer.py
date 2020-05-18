
from rest_framework import serializers

from .models import Banner,MoblieList,MiddleNavHeaderData,MiddleNavHeader
class BannerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Banner
        fields=["id","banner_url"]


class MoblieListSerializer(serializers.ModelSerializer):
    class Meta:
        model=MoblieList
        fields=["id","banner_url","name"]





'''
序列化从表
'''
class MiddleNavHeaderDataSerializer(serializers.ModelSerializer):

    class Meta:
        model=MiddleNavHeaderData
        fields=["title","price","images_url",'id']


'''
通过主表获得从表
'''
class MiddleNavHeaderSerializer(serializers.ModelSerializer):
    '''
    序列化从表

    '''
    mid_data=MiddleNavHeaderDataSerializer(many=True)

    class Meta:
        model=MiddleNavHeader
        fields=["id","title","mid_data"]
        depth=2