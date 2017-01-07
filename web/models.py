# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.tag_name


class Article(models.Model):
    title = models.CharField(max_length = 100)  #博客题目
    category = models.CharField(max_length = 50, blank = True)  #博客分类 可为空
    tag = models.ManyToManyField(Tag, blank=True)  # 博客标签 可为空
    date_time = models.DateTimeField(auto_now_add = True)  #博客日期
    content = models.TextField(blank = True, null = True)  #博客文章正文

    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id':self.id})
        return "http://127.0.0.1:8000%s" % path
    
    #python3使用__str__
    def __str__(self) :
        return self.title.encode('utf-8')

    class Meta:
        ordering = ['-date_time']

class BlogComment(models.Model):
    user_name = models.CharField('评论者名字', max_length=100)
    user_email = models.EmailField('评论者邮箱', max_length=255)
    body = models.TextField('评论内容')
    created_time = models.DateTimeField('评论发表时间', auto_now_add=True)
    article = models.ForeignKey('Article', verbose_name='评论所属文章', on_delete=models.CASCADE)

    def __str__(self):
        return self.body[:20]

