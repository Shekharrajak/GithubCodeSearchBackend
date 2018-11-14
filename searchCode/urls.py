from django.conf.urls import url
from searchCode import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^searchcode/$', views.searchCode, name='searchCode'),
]