from django.contrib import admin

# Register your models here.

from .models import Banner,MoblieList,MiddleNavHeader,MiddleNavHeaderMobile,AdsList
admin.site.register(Banner)



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

