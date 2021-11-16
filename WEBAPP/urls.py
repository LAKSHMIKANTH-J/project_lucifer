from django.urls import path
from WEBAPP.views import *
app_name='WEBAPP'

urlpatterns=[
 path('wish/',wish,name='wish'),
]