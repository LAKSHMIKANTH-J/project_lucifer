from django.urls import path
from WEBAPP2.views import *
app_name='WEBAPP2'

urlpatterns=[
 path('rama/',rama,name='rama')
]