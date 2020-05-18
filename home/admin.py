from django.contrib import admin

# Register your models here.

from .models import Banner,MoblieList,MiddleNavHeader,MiddleNavHeaderData
admin.site.register(Banner)

admin.site.register(MoblieList)


admin.site.register(MiddleNavHeader)



admin.site.register(MiddleNavHeaderData)