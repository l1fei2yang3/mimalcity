from django.contrib import admin

# Register your models here.

from .models import Banner,MoblieList
admin.site.register(Banner)

admin.site.register(MoblieList)