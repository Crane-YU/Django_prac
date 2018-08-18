from django.conf.urls import include, url
from django.contrib import admin

from teacher import views as tv
from teacher import teacher_url

urlpatterns = [
    # Examples:
    # url(r'^$', 'prac.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # 一个简单的映射，并无实际作用
    url(r'^normalmap/', tv.do_normalmap),

    # 比如约定，凡是由teacher模块处理的视图的url都以teacher开头
    url(r'^teacher/', include(teacher_url)),

    # url中的嵌套参数
    url(r'^book/(?:page-(?P<pn>\d+)/$)', tv.do_param2),

    # url中的额外参数
    url(r'^yourname/$', tv.extremparam, {"name": "Crane"}),

    # url反向解析：给url赋予一个名字，若url被修改也不会影响查找它的name
    url(r'^mayiknowyourname/$', tv.revParser, name = 'askname'),


]
