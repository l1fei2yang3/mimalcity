
from rest_framework.serializers import ModelSerializer

from .models import Banner,MoblieList
class BannerModelSerializer(ModelSerializer):
    class Meta:
        model=Banner
        fields=["id","banner_url"]


class MoblieListSerializer(ModelSerializer):
    class Meta:
        model=MoblieList
        fields=["id","banner_url","name"]