#!/usr/bin/env/
#coding:utf-8

"""study_cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from study_contents import views as sc_views #django1.11 引用方法


urlpatterns = [
    url(r'^$', sc_views.index, name='index'),
    url(r'^column/(?P<column_slug>[^/]+)/$', sc_views.column_detail, name='column_detail'),
    url(r'^article/(?P<article_slug>[^/]+)/$', sc_views.article_detail, name='article_detail'),

    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
	#    url(r'^ueditor/',include(DjangoUeditor_urls)),
]

from django.conf import settings

if settings.DEBUG:
	from django.conf.urls.static import static
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
