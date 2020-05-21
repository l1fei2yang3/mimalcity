

from rest_framework.serializers import ModelSerializer,ListSerializer

from .models import Product,ProductLunbo

class FilterLunboModelSerializer(ListSerializer):
    def to_representation(self, data):
        data=data.filter(is_show=True,is_delete=False)
        return super(FilterLunboModelSerializer, self).to_representation(data)



class ProductLunboModelSerializer(ModelSerializer):

    class Meta:
        model=ProductLunbo
        list_serializer_class=FilterLunboModelSerializer
        fields=["lb",'id']





class ProductListModelSerializer(ModelSerializer):
    product=ProductLunboModelSerializer(many=True)
    class Meta:
        model=Product
        fields=["product","name","sub_name","pfone","pftwo",'pfthree','pffour','price','img1','img2','img3',"video_img","video_des","sub_video_desc","video_url"

                ]