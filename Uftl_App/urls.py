from django.conf.urls import url
from django.urls import path
from Uftl_App import views

app_name = 'Uftl_App'

urlpatterns = [
   path('',views.index,name='index'),



]


