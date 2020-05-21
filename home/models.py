from django.db import models
from utils.models import BaseModel

class Banner(BaseModel):
    images=models.ImageField(upload_to="slide",verbose_name="轮播图图片地址",null=True,blank=True,help_text="轮播图")
    name=models.CharField(max_length=20,verbose_name="轮播图名称")
    discrible=models.CharField(max_length=50,verbose_name="轮播图描述")
    banner_url=models.CharField(max_length=30,verbose_name="轮播图广告地址")
    product_id=models.IntegerField(null=True,blank=True,verbose_name="产品id")
    class Meta:
        db_table="lbt"
        verbose_name="轮播图"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name



class LeftMenu(BaseModel):
    title = models.CharField(max_length=30, verbose_name="左侧标题")
    class Meta:
        db_table = "left_title"
        verbose_name = "左侧菜单"
        verbose_name_plural = verbose_name



class MoblieList(BaseModel):
    images = models.ImageField(upload_to="mobile",verbose_name="手机图片地址",null=True,blank=True)
    name = models.CharField(max_length=30, verbose_name="手机图片名称")
    discrible = models.CharField(max_length=150, verbose_name="手机图片描述")
    banner_url = models.CharField(max_length=150, verbose_name="手机广告地址")
    lmenu=models.ForeignKey("LeftMenu",on_delete=models.CASCADE,related_name="lmenu",null=True,blank=True)
    product_id = models.IntegerField(null=True, blank=True, verbose_name="产品id")
    class Meta:
        db_table="menu"
        verbose_name="菜单"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name

class MiddleNavHeader(BaseModel):
    title=models.CharField(max_length=20,verbose_name="导航栏标题名称")
    class Meta:
        db_table="mnav"
        verbose_name="中部导航栏标题"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.title

class MiddleNavHeaderMobile(BaseModel):
    images=models.ImageField(upload_to="nav-img",verbose_name="中部导航栏图片",null=True,blank=True)
    title=models.CharField(max_length=20,verbose_name="中部导航栏标题")
    price=models.IntegerField(verbose_name="中部导航栏价格")
    midheader=models.ForeignKey("MiddleNavHeader",on_delete=models.CASCADE,verbose_name="外键关联中部标题",related_name="mid_header")
    images_url=models.CharField(max_length=120,null=True,blank=True)
    product_id = models.IntegerField(null=True, blank=True, verbose_name="产品id")
    class Meta:
        db_table="mnav_header"
        verbose_name="中部导航栏数据"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.title


class AdsList(BaseModel):
    images=models.ImageField(upload_to="ads",verbose_name="广告位上传图片",null=True,blank=True,help_text="广告位上传图片")
    images_url=models.CharField(max_length=100)
    product_id = models.IntegerField(null=True, blank=True, verbose_name="产品id")
    class Meta:
        db_table="ads"
        verbose_name="广告表"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.images_url

class MiddleAdsList(BaseModel):
    images=models.ImageField(upload_to="mads",verbose_name="广告位上传图片",null=True,blank=True,help_text="广告位上传图片")
    images_url=models.CharField(max_length=100)
    product_id = models.IntegerField(null=True, blank=True, verbose_name="产品id")
    class Meta:
        db_table="midads"
        verbose_name="中部广告表"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.images_url

class LeftBottomAdsList(BaseModel):
    images = models.ImageField(upload_to="lads", verbose_name="广告位上传图片", null=True, blank=True, help_text="广告位上传图片")
    images_url = models.CharField(max_length=100)
    product_id = models.IntegerField(null=True, blank=True, verbose_name="产品id")

    class Meta:
        db_table = "lbads"
        verbose_name = "左下部广告表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.images_url


class RightBottomAdsList(BaseModel):


    title=models.CharField(max_length=50,null=True,blank=True,verbose_name="标题")
    discrable=models.CharField(max_length=50,null=True,blank=True,verbose_name="描述")
    price=models.IntegerField(null=True,blank=True,verbose_name="价格")
    is_new=models.CharField(max_length=20,null=True,blank=True,verbose_name="是否是新品")
    color=models.CharField(max_length=20,null=True,blank=True,verbose_name="秒杀颜色选项")
    images = models.ImageField(upload_to="rads", verbose_name="广告位上传图片", null=True, blank=True, help_text="广告位上传图片")
    images_url = models.CharField(max_length=100)
    product_id = models.IntegerField(null=True, blank=True, verbose_name="产品id")

    class Meta:
        db_table = "rbads"
        verbose_name = "右下部广告表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title








