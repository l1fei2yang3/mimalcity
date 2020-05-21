from django.urls import path

from product.views import ProductListAPIView

urlpatterns=[
    path("info/",ProductListAPIView.as_view())
]