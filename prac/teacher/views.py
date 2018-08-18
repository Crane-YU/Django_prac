from django.shortcuts import render
from django.http import HttpResponse

from django.core.urlresolvers import reverse

# Create your views here.

'''
视图需要一个参数，类型应该是HttpRequest，就是传入的请求
'''


def do_normalmap(request):
    return HttpResponse("this is normal map")


def withparam(request, year, month):
    return HttpResponse("this is param {0} and {1}".format(year, month))


def do_app(request):
    return HttpResponse("这是一个子路由")


def do_param2(request, pn):
    return HttpResponse("Page number is {0}".format(pn))


def extremparam(request, name):
    return HttpResponse("My name is {0}".format(name))


def revParser(request):
    return HttpResponse("Your request url is: {0}".format(reverse('askname')))