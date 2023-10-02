from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name ='index'),
    path('delete/<int:id>/',delete, name ='delete'),
    path('create/',create, name ='create'),
    path('update/<int:id>/',update, name ='update'),
    path('profDetails/<int:id>/',profileDetails, name ='profDetails'),
    path('cal/',cal, name ='cal'),
    path('converter/',converter, name ='converter'),
    path('downloader/',downloader, name ='downloader'),
]