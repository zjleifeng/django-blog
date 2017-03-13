#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-3-2 下午5:28
# @Author  : eric
# @Site    :
# @File    : models.py
# @Software: PyCharm

from django.db import models
from myblog import settings
import os
from PIL import Image
from django.db.models.fields.files import ImageFieldFile
# Create your models here.



#对上传的图片进行裁剪
def make_pic(path,stup):
    pixbuf = Image.open(path)
    wsize=pixbuf.size[0]
    hsize=pixbuf.size[1]
    ywith=stup[0]
    yhigh=stup[1]
    if wsize/hsize>ywith/yhigh:
        wnew=hsize*ywith/yhigh
        #offset = int(pixbuf.size[0] - pixbuf.size[1]) / 2
        newimg = pixbuf.transform((wnew, hsize), Image.EXTENT, ((wsize-wnew)/2,0,wnew+(wsize-wnew)/2, hsize))
        #newimg.thumbnail((700, 400), Image.ANTIALIAS)
    else:
        hnew=wsize*yhigh/ywith
        newimg = pixbuf.transform((wsize,hnew), Image.EXTENT, (0,(hsize-hnew)/2,wsize,hnew+(hsize-hnew)/2))
        newimg.thumbnail((ywith, yhigh), Image.ANTIALIAS)


    #newimg.thumbnail((700, 400),Image.ANTIALIAS)



    return newimg




#n文章等发布内容的状态
STATUS={
    0:u'正常',
    1:u'草稿',
    2:u'删除',
}


#tag标签
class Tag(models.Model):
    name=models.CharField(max_length=30,verbose_name=u'标签名称')
    create_time=models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间')
    class Meta:
        verbose_name_plural=u'标签管理'

    def __unicode__(self):
        return self.name

    __str__=__unicode__


#分类
class Category(models.Model):
    name=models.CharField(max_length=30,unique=Tag,verbose_name=u'分类名称')
    parent=models.ForeignKey('self',default=None,blank=True,null=True,on_delete=models.SET_NULL,verbose_name=u'上级分类')
    rank=models.IntegerField(default=0,verbose_name=u'排序')
    #status=models.IntegerField(default=2,choices=STATUS.items(),verbose_name=u'状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')

    class Meta:
        verbose_name_plural=u'分类管理'
        ordering=['-create_time']

    def __unicode__(self):
        if self.parent:
            return '%s-->%s' % (self.parent,self.name)
        else:
            return self.name
    __str__=__unicode__


#文章MODEL
class Article(models.Model):
    title=models.CharField(max_length=50,verbose_name=u'文章标题')
    desc=models.CharField(max_length=100,blank=True,null=True,verbose_name=u'文章描述')
    content=models.TextField(verbose_name=u'文章内容')
    img=models.ImageField(verbose_name=u'缩略图',upload_to='./article',blank=True,null=True)
    category=models.ForeignKey(Category,blank=True,null=True,on_delete=models.SET_NULL,verbose_name=u'分类')
    tags=models.ManyToManyField(Tag,verbose_name=u'标签')
    author=models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name=u'作者')
    chick_count=models.IntegerField(default=0,verbose_name=u'点击次数')
    zan_times=models.IntegerField(default=0,verbose_name=u'被赞次数')
    is_top=models.BooleanField(default=False,verbose_name=u'是否置顶')
    rank=models.IntegerField(default=0,verbose_name=u'排序')
    create_time=models.DateTimeField(auto_now_add=True,verbose_name=u'创建时间')
    status=models.IntegerField(default=0,choices=STATUS.items(),verbose_name=u'文章状态')

    class Meta:
        verbose_name_plural=u'文章管理'
        ordering=['rank','-is_top','-create_time']

    def save(self):
        if self.img.width>480:

            small_path='uploads/article/small'
            x='uploads/article/small/'
            super(Article,self).save()

            base,ext= os.path.splitext(os.path.basename(self.img.path))
            thumb_pixbuf=make_pic(os.path.join(settings.MEDIA_ROOT,self.img.name),(480,260))
            relate_thumb_path=os.path.join(small_path,base+'.article'+ext)
            thumb_path=os.path.join(relate_thumb_path)
            thumb_pixbuf.save(thumb_path)
            self.img=ImageFieldFile(self,self.img,x+base+'.article'+ext)
        super(Article,self).save()

    def __unicode__(self):
        return self.title
    __str__=__unicode__


#评论
class Comment(models.Model):
    content=models.TextField(verbose_name=u'评论内容')
    username=models.CharField(max_length=30,blank=True,null=True,verbose_name=u'用户名')
    email=models.EmailField(max_length=50,blank=True,null=True,verbose_name=u'邮箱地址')
    siteurl=models.URLField(max_length=50,blank=True,null=True,verbose_name=u'个人网站地址')
    authuser=models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True,verbose_name=u'作者')
    article=models.ForeignKey(Article,blank=True,null=True,verbose_name=u'所属文章')
    parent=models.ForeignKey('self',blank=True,null=True,verbose_name=u'父级评论')
    status = models.IntegerField(default=0, choices=STATUS.items(), verbose_name=u'状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')

    class Meta:
        verbose_name_plural=u'评论管理'
        ordering=['-create_time']
    def __unicode__(self):
        return self.content
    __str__=__unicode__


#友情链接
class Links(models.Model):
    name=models.CharField(max_length=50,verbose_name=u'链接名称')
    des=models.CharField(max_length=200,verbose_name=u'链接说明')
    siteurl=models.URLField(verbose_name=u'链接地址')
    rank=models.IntegerField(default=0,verbose_name=u'排序')
    status = models.IntegerField(default=0, choices=STATUS.items(), verbose_name=u'状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')

    class Meta:
        verbose_name_plural=u'友情链接'
        ordering=['rank']
    def __unicode__(self):
        return self.name
    __str__=__unicode__

#留言板
class MsgBook(models.Model):
    name=models.CharField(max_length=20,blank=True,null=True,verbose_name=u'昵称')
    content = models.TextField(verbose_name=u'留言内容')
    email=models.EmailField(max_length=50,blank=True,null=True,verbose_name=u'邮箱地址')
    siteurl=models.URLField(max_length=50,blank=True,null=True,verbose_name=u'个人网站地址')
    authuser=models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True,verbose_name=u'作者')
    parent=models.ForeignKey('self',blank=True,null=True,verbose_name=u'父级留言')
    status = models.IntegerField(default=0, choices=STATUS.items(), verbose_name=u'状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')


    class Meta:
        verbose_name_plural = u'留言'
        ordering = ['-create_time']


    def __unicode__(self):
        return self.content


    __str__ = __unicode__


#广告发布
class Advert(models.Model):
    title=models.CharField(max_length=50,verbose_name=u'广告标题')
    des=models.TextField(max_length=300,verbose_name=u'广告描述')
    image_url=models.ImageField(upload_to='uploads/ad/%Y/%m',verbose_name=u'广告图片')
    callback_url=models.URLField(blank=True,null=True,verbose_name=u'回调URL')
    rank=models.IntegerField(default=0,verbose_name=u'排序')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')

    class Meta:
        verbose_name_plural=u'广告管理'
        ordering=['rank']

    def __unicode__(self):
        return self.title
    __str__=__unicode__



IS_READ = {
        0: u'未读',
        1: u'已读'
}


class Notification(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    text = models.TextField(verbose_name=u'内容')
    url = models.CharField(max_length=200, verbose_name=u'连接',
                           null=True, blank=True)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  default=None, blank=True, null=True,
                                  related_name='from_user_notification_set',
                                  verbose_name=u'发送者')
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                related_name='to_user_notification_set',
                                verbose_name=u'接收者')
    type = models.CharField(max_length=20, verbose_name=u'类型',
                            null=True, blank=True)

    is_read = models.IntegerField(default=0, choices=IS_READ.items(),
                                  verbose_name=u'是否读过')

    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True)

    class Meta:
        verbose_name_plural = verbose_name = u'消息'
        ordering = ['-create_time']



class Aboutme(models.Model):
    name=models.CharField(max_length=20,verbose_name=u'姓名')
    nickname=models.CharField(max_length=30,verbose_name=u'昵称')
    sitename=models.CharField(max_length=30,verbose_name=u'个人网站名称')
    sitedes=models.CharField(default="无",max_length=50,verbose_name=u'站点简介')
    siteurl=models.URLField(verbose_name=u'个人网站地址')
    content=models.TextField(max_length=2000,verbose_name=u'个人自我介绍')
    uselan=models.CharField(max_length=100,verbose_name=u'程序语言')
    status = models.IntegerField(default=0, choices=STATUS.items(), verbose_name=u'状态')
    class Meta:
        verbose_name_plural=u'自我介绍'


    def __unicode__(self):
        return self.nickname
    __str__=__unicode__