# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from django.shortcuts import render

# Create your views here.

def home(request):

    return render(request, 'base.html', {})
