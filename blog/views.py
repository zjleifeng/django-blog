#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-3-2 下午5:28
# @Author  : eric
# @Site    :
# @File    : views.py
# @Software: PyCharm

from django.shortcuts import render
from django.core.cache import caches
from myblog import settings
from blog.models import Article,Comment,Links,Tag,Category,Aboutme
from django.views.generic import TemplateView,ListView,DetailView,View
from django.db.models import Q
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django import template
import json
import logging
import re
# Create your views here.
#缓存
try:
    cache=caches['mencache']
except ImportError as e:
    cache=caches['default']


#logger
logger = logging.getLogger(__name__)


class BaseMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super(BaseMixin, self).get_context_data(**kwargs)
        try:
            # 网站标题等内容
            context['website_title'] = settings.WEBSITE_TITLE
            context['website_name'] = settings.WEBSITE_NAME
            context['PAGE_NUM']=settings.PAGE_NUM
            # 热门文章
            context['hot_article_list'] = \
                Article.objects.order_by("-chick_count")[0:10]

            # 最新评论
            context['latest_comment_list'] = \
                Comment.objects.order_by("-create_time")[0:10]
            # 友情链接
            context['links'] = Links.objects.all()
            # 分类
            context["r_category_list"] = Category.objects.order_by("-rank").all()
            # 标签
            context["r_tags_list"] = Tag.objects.all()


            #读取文章按月份归类
            articles = Article.objects.all()
            year_month = set()  # 设置集合，无重复元素
            for a in articles:

                year_month.add((a.create_time.year, a.create_time.month))  # 把每篇文章的年、月以元组形式添加到集合中
            counter = {}.fromkeys(year_month, 0)  # 以元组作为key，初始化字典
            for a in articles:
                counter[(a.create_time.year, a.create_time.month)] += 1  # 按年月统计文章数目
            year_month_number = []  # 初始化列表
            for key in counter:
                year_month_number.append({"year":key[0],"month":key[1],"count":counter[key]})
                #year_month_number.append([key[0], key[1], counter[key]])  # 把字典转化为（年，月，数目）元组为元素的列表
            year_month_number.sort(reverse=True)  # 排序

            context["year_month_number"]=year_month_number



            #读取用户IP
            if self.request.META.has_key('HTTP_X_FORWARDED_FOR'):
                ip = self.request.META['HTTP_X_FORWARDED_FOR']
            else:
                ip = self.request.META['REMOTE_ADDR']
            context['ip_adress']=ip

            # 用户未读消息数
            user = self.request.user
            if user.is_authenticated():
                context['notification_count'] = \
                    user.to_user_notification_set.filter(is_read=0).count()
        except Exception as e:
            logger.error(u'[BaseMixin]加载基本信息出错')

        return context


#首页
class IndexView(BaseMixin, ListView):
    template_name = 'index.html'
    context_object_name = 'obj_list'
    paginate_by = settings.PAGE_NUM  # 分页--每页的数目

    def get_context_data(self, **kwargs):
        kwargs['sec_list']="首页"
        kwargs['tags'] = Tag.objects.all()
        kwargs['indexclass']="current"
        return super(IndexView, self).get_context_data(**kwargs)

    def get_queryset(self):
        obj_list = Article.objects.filter(status=0)
        return obj_list




#文章
class ArticleView(BaseMixin,DetailView):
    queryset = Article.objects.filter(status=0)
    template_name = 'include/article.html'
    context_object_name = 'article_list'
    slug_field = 'pk'

    def get(self,request,*args,**kwargs):
        #统计文章访问次数
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        self.cur_user_ip = ip

        en_id=self.kwargs.get("pk")
        visited_ips=cache.get(en_id,[])

        #如果IP不存在则加1
        if ip not in visited_ips:
            try:
                article=self.queryset.get(id=en_id)
            except Article.DoesNotExist:
                pass
                raise Http404
            else:
                article.chick_count +=1
                article.save()
                visited_ips.append(ip)

            cache.set(en_id,visited_ips,15*60)

        return super(ArticleView,self).get(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        #获取评论
        en_id=self.kwargs.get('pk',"")
        try:
            article=Article.objects.get(pk=en_id)
            comments=Comment.objects.filter(article=article)
            comment_list=[]
            for comment in comments:
                for item in comments:
                    if not hasattr(item,'children_comment'):
                        setattr(item,'children_comment',[])
                    if comment.parent==item:
                        item.children_comment.append(comment)
                        break
                if comment.parent is None:
                    comment_list.append(comment)
            comment_len=len(comment_list)
            kwargs['comment_list'] = comment_list
        except Article.DoesNotExist:
            pass


        #kwargs['comment_list']=self.queryset.get(id=en_id).comment_set.all()

        return super(ArticleView,self).get_context_data(**kwargs)

class AllView(BaseMixin,ListView):
    template_name = 'include/all_article.html'
    context_object_name = 'obj_list'

    def get_context_data(self, **kwargs):

        kwargs['sec_list']='博文'
        kwargs['category_list']=Category.objects.all()
        kwargs['PAGE_NUM']=settings.PAGE_NUM
        kwargs['allclass'] = "current"
        return super(AllView,self).get_context_data(**kwargs)

    def get_queryset(self):
        obj_list=Article.objects.filter(status=0).order_by('-create_time')[0:settings.PAGE_NUM]
        return obj_list

    def post(self,request,*args,**kwargs):
        val=self.request.POST.get('val','')
        start = self.request.POST.get("start", 0)
        end = self.request.POST.get("end", settings.PAGE_NUM)

        start = int(start)
        end = int(end)
        if val=="all":
            obj_list=Article.objects.filter(status=0).order_by('-create_time')[0:end]
        else:
            try:
                obj_list=Category.objects.get(name=val).article_set.filter(status=0).order_by("-create_time")[start:end+1]
            except Category.DoesNotExist:
                pass
                raise Http404

        isend = len(obj_list) != (end - start + 1)

        obj_list = obj_list[0:end - start]
        html=""
        for obj in obj_list:
            html+=template.loader.get_template(
                'include/post_article.html'
            ).render(template.Context({'obj':obj}))

        if html=="":
            html="暂无此类文章"
        mydict={"html":html,"isend": isend,'sec_list':"sss"}
        return HttpResponse(json.dumps(mydict),content_type='application/json')

class PostCommentView(View):
    def post(self,request,*args,**kwargs):
        user=self.request.user
        if not user.is_authenticated():
            userauth=None
        else:
            userauth=user
        content=self.request.POST.get("comment", "")
        username=self.request.POST.get("inputName", "")
        email=self.request.POST.get("inputEmail", "")
        website=self.request.POST.get("inputWebsite", "")
        parent=self.request.POST.get("disid","")

        en_id=self.kwargs.get('slug','')
        try:
            article=Article.objects.get(id=en_id)
        except Article.DoesNotExist:
            pass
        if content==""or username=="":
            return HttpResponse('评论需要填写昵称和评论内容！')
        parent_comment=None
        if parent:
            parent_id=int(parent)
            try:
                parent_comment=Comment.objects.get(pk=parent_id)
            except Comment.DoesNotExist:
                return HttpResponse("错误！")
        comment=Comment.objects.create(
            username=username,content=content,email=email,siteurl=website,authuser=userauth,article=article,parent=parent_comment
        )
        print_comment=u''
        if parent:
            print_comment=u""


        return HttpResponseRedirect("/")


#搜索
class SearchView(BaseMixin,ListView):
    template_name = 'include/all_article.html'
    context_object_name = 'obj_list'
    paginate_by = settings.PAGE_NUM

    def get_context_data(self, **kwargs):
        kwargs['first_list'] = "搜索"
        kwargs["sec_list"] = self.request.GET.get("word","")
        kwargs["word"]=self.request.GET.get("word","")
        kwargs['category_list'] = Category.objects.all()
        return super(SearchView,self).get_context_data(**kwargs)

    def get_queryset(self):
        word=self.request.GET.get("word",'')

        obj_list=Article.objects.filter(
            Q(title__icontains=word)|Q(desc__icontains=word),status=0
        )

        return obj_list

#分类查询
class CaregoryView(BaseMixin,ListView):
    template_name = 'index.html'
    context_object_name = 'obj_list'
    paginate_by = settings.PAGE_NUM

    def get_context_data(self, **kwargs):
        en_id = self.kwargs.get('pk', "")
        kwargs['tags'] = Tag.objects.all()
        kwargs['category_list'] = Category.objects.all()
        kwargs['first_list']="文章分类"
        kwargs["sec_list"]=Category.objects.get(id=en_id).name
        return super(CaregoryView,self).get_context_data(**kwargs)

    def get_queryset(self):
        en_id=self.kwargs.get('pk',"")

        try:
            obj_list=Category.objects.get(pk=en_id).article_set.all()
        except Category.DoesNotExist:
            pass

        return obj_list


#标签查询
class TagsView(BaseMixin,ListView):
    template_name = 'index.html'
    context_object_name = 'obj_list'

    def get_context_data(self, **kwargs):
        en_tag = self.kwargs.get("tag_name", "")
        kwargs['tags'] = Tag.objects.all()
        kwargs['category_list'] = Category.objects.all()
        kwargs['first_list']="标签"
        kwargs["sec_list"]=en_tag
        return super(TagsView,self).get_context_data(**kwargs)

    def get_queryset(self):
        en_tag=self.kwargs.get("tag_name","")
        try:
            tags=Tag.objects.get(name=en_tag)
            obj_list=Article.objects.filter(tags=tags)
        except Tag.DoesNotExist:
            pass
        return obj_list

#按时间归类
class DateArticleView(BaseMixin,ListView):
    template_name = 'index.html'
    context_object_name = 'obj_list'

    def get_context_data(self, **kwargs):
        en_year = self.kwargs.get("year", "")
        en_month = self.kwargs.get("month", "")
        kwargs["first_list"]="时间归类"
        kwargs["sec_list"]=en_year+'/'+en_month
        kwargs['tags'] = Tag.objects.all()
        kwargs['category_list'] = Category.objects.all()
        return super(DateArticleView,self).get_context_data(**kwargs)
    def get_queryset(self):

        en_year=self.kwargs.get("year","")
        en_month=self.kwargs.get("month","")
        if int(en_month)<10:
            strmonth="0"+en_month
        obj_list=Article.objects.filter(create_time__icontains=en_year+'-'+strmonth)
        return obj_list

class AboutMeView(BaseMixin,ListView):
    queryset = Aboutme.objects.filter(status=0)
    template_name = 'include/aboutme_post.html'
    context_object_name = 'obj_list'


    def get_context_data(self, **kwargs):
        kwargs['aboutclass']="current"
        return super(AboutMeView,self).get_context_data(**kwargs)

    def get_queryset(self):
        if self.queryset:
            obj_list=self.queryset[0]
        return obj_list