from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from .models import Product
from rest_framework.generics import ListAPIView

from rest_framework.response import Response
from .serializer import ProductListModelSerializer
class ProductListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        id = request.query_params.get("id")
        pro = Product.objects.filter(is_show=True, is_delete=False,id=id)
        pet=ProductListModelSerializer(pro,many=True)
        # print(pet.data)
        return Response(pet.data)





