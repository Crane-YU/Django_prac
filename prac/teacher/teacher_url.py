from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'prac.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # 一个简单的映射，并无实际作用
    url(r'^crane/', views.do_app),
    #url(r'^normalmap/', tv.do_normalmap),
    #url(r'^withparam/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])', tv.withparam),
]