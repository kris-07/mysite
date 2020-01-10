from django.urls import path
from . import views

urlpatterns=[
    path('registration/',views.register, name='register'),
    path('validation/',views.validation, name='validation'),
    #path('userinfo/', views.userinfo, name='userinfo')
]