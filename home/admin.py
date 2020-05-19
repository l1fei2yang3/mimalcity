from django.contrib import admin

# Register your models here.

from .models import Banner,MoblieList,MiddleNavHeader,MiddleNavHeaderMobile,AdsList,MiddleAdsList\
    ,LeftBottomAdsList,RightBottomAdsList,LeftMenu


'''
轮播图列表
'''
admin.site.register(Banner)



'''
手机左侧菜单列表 
'''


admin.site.register(LeftMenu)


'''
手机菜单列表 
'''


admin.site.register(MoblieList)

'''
首页中部导航栏
'''
admin.site.register(MiddleNavHeader)



admin.site.register(MiddleNavHeaderMobile)


'''
首页广告位
'''

admin.site.register(AdsList)


'''
中部广告位
'''

admin.site.register(MiddleAdsList)


'''
左下部广告位 
'''

admin.site.register(LeftBottomAdsList)

'''
右下部广告位 
'''
admin.site.register(RightBottomAdsList)

