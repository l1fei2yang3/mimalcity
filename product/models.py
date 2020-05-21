from django.db import models

# Create your models here.
from utils.models import BaseModel

'''
产品表

'''
class Product(BaseModel):
    name = models.CharField(max_length = 50,null = True,blank = True,verbose_name = "产品名称")
    sub_name = models.CharField(max_length = 50,null = True,blank = True,verbose_name = "产品副标题")
    pfone = models.CharField(max_length = 100,verbose_name = "产品特性1",null = True,blank = True)
    pftwo = models.CharField(max_length = 100,verbose_name = "产品特性2",null = True,blank = True)
    pfthree = models.CharField(max_length = 100,verbose_name = "产品特性3",null = True,blank = True)
    pffour = models.CharField(max_length = 100,verbose_name = "产品特性4",null = True,blank = True)
    price = models.IntegerField(verbose_name = "价格",null = True,blank = True)
    img1 = models.ImageField(upload_to = "imgs/product",verbose_name="大图片1",null = True,blank = True)
    img2 = models.ImageField(upload_to = "imgs/product",verbose_name="大图片2",null = True,blank = True)
    img3 = models.ImageField(upload_to = "imgs/product",verbose_name="大图片3",null = True,blank = True)
    video_img=models.ImageField(upload_to="imgs/product",verbose_name="视频背景图",null = True,blank = True)
    video_des = models.CharField(max_length = 100,verbose_name="视频主描述",null = True,blank = True)
    sub_video_desc = models.CharField(max_length = 300,verbose_name = "视频副描述",null = True,blank = True)
    video_url = models.FileField(upload_to ="imgs/product",verbose_name = "视频上传路径",null = True,blank = True)
    class Meta:
        db_table = "product"
        verbose_name = "产品表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name


class ProductLunbo(BaseModel):
    lb = models.ImageField(upload_to="imgs/product", verbose_name="轮播图1", null=True, blank=True)

    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="product")
    class Meta:
        db_table="plb"
        verbose_name="产品页轮播图"
        verbose_name_plural=verbose_name



