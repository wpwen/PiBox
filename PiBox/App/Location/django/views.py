#coding=utf-8
from django.shortcuts import render
from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.utils import simplejson  

from PiApp.forms import *
from PiApp.models import *
from PiApp.app import *
from PiApp.utils import *
import PiApp.gl



def Location(request):
    t = get_template('application/Location/django/html/location.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))