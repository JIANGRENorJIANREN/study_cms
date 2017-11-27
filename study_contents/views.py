# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
	return HttpResponse(u'欢迎来自强学堂学习Django')


def column_detail(request, column_slug):
	return HttpResponse('column slug: ' + column_slug)


def article_detail(request, article_slug):
	return HttpResponse('article slug: ' + article_slug)