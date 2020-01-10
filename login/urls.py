from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns=[
    path('',views.login, name='login'),
    path('userinfo/', views.userinfo, name='userinfo'),
    url(r'^(?P<id>\d+)/$', views.userinfo)
]