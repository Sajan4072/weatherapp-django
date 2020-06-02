from django.urls import path
from . import views

urlpatterns= [
    path('',views.index,name='index'),
    path('delete/<place_name>/',views.delete_place,name='delete_place')

]