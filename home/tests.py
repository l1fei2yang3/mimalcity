import os
from home.models import MoblieList
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mimal.settings")
django.setup()



# from django.test import TestCase
#
# # Create your tests here.
a=0
b=5
from datetime import datetime
# while a<5:
MoblieList.objects.create(order=5,is_delete=False,create_time=datetime.now(),updated_time=datetime.now(),images="mobile/item-box-2.png",name="小米青春版",discrible="xxx",banner_url="/imgs/item-box-2.png")

