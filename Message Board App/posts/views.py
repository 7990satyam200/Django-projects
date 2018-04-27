# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import Post

class func(ListView):
    model=Post
    template_name='home.html'
