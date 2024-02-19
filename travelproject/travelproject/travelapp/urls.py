
from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('demo/',views.demo,name='demo'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
]

