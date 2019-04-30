from django.conf.urls import url,include
from help import views

urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^articles/$', views.articles, name='articles'),
]