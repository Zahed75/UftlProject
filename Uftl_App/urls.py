from django.conf.urls import url
from django.urls import path
from Uftl_App import views

app_name = 'Uftl_App'

urlpatterns = [
   path('',views.index,name='index'),
   # path('index/',views.index,name='index'),
   path('assets/',views.assets,name='assets'),
   path('contact_page/',views.contact_page,name='contact_page'),

]


