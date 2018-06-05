from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
app_name="booktest"
urlpatterns = [
    path('', views.index2),
    url(r'^(\d+)/(\d+)/$', views.showrec, name="showrec"),
    url(r'^(\d+)/$', views.show, name="show"),
    url(r'^user1/$',views.user1, name='user'),
    url(r'^user2/$', views.user2, name='user2'),
    url(r'^csrf1/$', views.csrf1, name='csrf1'),
    url(r'^csrf2/$', views.csrf2, name='csrf2'),
    url(r'^verifycode/$', views.verifycode, name='verifycode'),

]
