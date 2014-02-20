from django.shortcuts import render_to_response,HttpResponse,Http404
##from django.contrib import auth
from lib.models import Article,Article_class
from django.db import models

def render_index(request):
    args={}
    args['current_site']='home'
    args['title']='Home of DjWong\'s Tech Blog'
    args['articles']=Article.objects.all()
    args['perms']=request.user.get_all_permissions()
    return render_to_response('index.html',args)

def search(request):
    args={}
    args['title']='Search Result'
    if 'q' in request.GET and request.GET['q']:
        articles=Article.objects.filter(title__contains=request.GET['q'])|Article.objects.filter(content__contains=request.GET['q'])
        args['articles']=articles
        return render_to_response('index.html',args)
    else:
        return render_to_response('index.html',args)

def render_category(request,category_id):
    args={}
    args['title']='Category:'
    try:
        category_id=int(category_id)
    except ValueError:
        return render_to_response('index.html',args)
    articles=Article.objects.filter(aclass=category_id)
    aclass=Article_class.objects.get(cid=category_id)
    args['title']+=aclass.name
    args['articles']=articles
    return render_to_response('index.html',args)

def render_author(request,author_name):
    args={}
    args['title']='Author:'+author_name
    articles=Article.objects.filter(author=author_name)
    args['articles']=articles
    return render_to_response('index.html',args)
def render_feeds(request):
    pass
