# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from study_contents.models import Column, Article

# Create your views here.
def index(request):
	#return HttpResponse(u'欢迎来自强学堂学习Django')
	#columns = Column.objects.all()
	home_display_columns = Column.objects.filter(home_display=True)
	nav_display_columns = Column.objects.filter(nav_display=True)

	return render(request, 'index.html', {
		'home_display_columns':home_display_columns,
		'nav_display_columns':nav_display_columns,
	})


def column_detail(request, column_slug):
	column = Column.objects.get(slug=column_slug)
	return render(request,'study_contents/column.html',{'column':column})


def article_detail(request, pk, article_slug):
	#return HttpResponse('article slug: ' + article_slug)
	article = Article.objects.get(pk=pk)

	if article_slug != article.slug:
		return redirect(article, permanent=True)
	return render(request,'study_contents/article.html',{'article':article})

