# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.utils.encoding import python_2_unicode_compatible
from DjangoUeditor.models import UEditorField
from django.core.urlresolvers import reverse

'''
知识点1:装饰器(decorator)是一种在代码运行期间动态增加功能的方式
知识点2:python_2_unicode_compatible作用为保持向后兼容，以后
	　　代码升级到３.x后执行也不会出问题
知识点3:每个应用一般都会定义一个或多个models，这个数据models实际
	　　上是与数据库相关的，models中的每个属性都是数据库当中的一个字段，
	　　每个字段是数据库中的一个列。在models中定义的每个类相当于数据库当中的table
知识点4:def __str__(self),__xx__成为魔幻方法，每个魔法方法都是在对内建方法的重写，
	　　和做像装饰器一样的行为。
'''

@python_2_unicode_compatible
class Column(models.Model):
	name = models.CharField('栏目名称',max_length = 256)
	slug = models.CharField('栏目网址',max_length = 256,db_index = True)
	intro = models.TextField('栏目简介',default='')

	nav_display = models.BooleanField('导航显示',default=False)
	home_display = models.BooleanField('首页显示',default=False)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = '栏目'
		verbose_name_plural = '栏目'
		ordering = ['name']

	def get_absolute_url(self):
		return reverse('column',args=(self.slug,))


@python_2_unicode_compatible
class Article(models.Model):
	column = models.ManyToManyField(Column,verbose_name='归属栏目')

	title = models.CharField('标题',max_length=256)
	slug = models.CharField('网址',max_length=256,db_index=True)

	author = models.ForeignKey('auth.User',blank=True,null=True,verbose_name='作者')
	#content = models.TextField('内容',default='',blank=True)
	content = UEditorField('内容', height=300, width=1000,
	                       default=u'', blank=True, imagePath="uploads/images/",
	                       toolbars='besttome', filePath='uploads/files/')
	published = models.BooleanField('正式发布',default=True)

	pub_date = models.DateTimeField('发表时间',auto_now_add=True,editable=True)
	update_time = models.DateTimeField('更新时间',auto_now=True,null=True)


	def __str__(self):
		return self.title

	class Meta:
		verbose_name = '从这里开始'
		verbose_name_plural = '教程'    #plural:复数形式

	def get_absolute_url(self):
		return reverse('article',args=(self.pk, self.slug))