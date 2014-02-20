from django.http import Http404,HttpResponse,HttpResponseRedirect
from lib import models
from django.shortcuts import render_to_response,render
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import user_passes_test
from lib.models import *
from datetime import datetime
from django.core.context_processors import csrf
from django.views.decorators.csrf import requires_csrf_token
from django.core.validators import email_re
from lib.functions import *

def show_article(request,article_id):
    try:
        article_id=int(article_id)
    except ValueError:
        raise Http404()
    try:
        article=Article.objects.get(tid=article_id)
        result={}
        result.update(csrf(request))
        result['article']=article
        result['perms']=request.user.get_all_permissions()
        result['comments']=Comment.objects.filter(tid=article_id)
        return render_to_response('article.html',result)
    except Article.DoesNotExist:
        raise Http404()

@user_passes_test(lambda u: u.has_perm("lib.add_article"),login_url='/admin/')
def post(request):
    classes=[]
    result={}
    result.update(csrf(request))
    for item in Article_class.objects.all():
        classes.append({'id':item.cid,'name':item.name})
    result['classes']=classes
    if not ('title' in request.POST and 'content' in request.POST):
        return render_to_response('post.html',result)
    errors=[]
    if not request.POST['title']:
        errors.append('Title is empty')
    if not request.POST['content']:
        errors.append('Content is empty')
    if errors==[]:
        article=Article(img=request.POST['img'],title=request.POST['title'],content=request.POST['content'],author=request.user.username,time_stamp=datetime.now(),comments=0,aclass=Article_class.objects.get(cid=request.POST['class']))
        article.save()
        errors.append('Published successfully')
    result['errors']=errors
    return render_to_response('post.html',result)



@user_passes_test(lambda u: u.has_perm("lib.change_article"),login_url='/admin/')
def edit(request,article_id):
    result={}
    result.update(csrf(request))
    try:
        article_id=int(article_id)
    except ValueError:
        raise Http404()
    try:
        articles=Article.objects.get(tid=article_id)
        result['content']=articles.content
        result['title']=articles.title 
        return render_to_response('edit.html',result)
    except Article.DoesNotExist:
        raise Http404()

@user_passes_test(lambda u: u.has_perm("lib.delete_article"),login_url='/admin/')
def delete(request,article_id):
    try:
        article_id=int(article_id)
    except ValueError:
        raise Http404()
    try:
        articles=Article.objects.get(tid=article_id)
        articles.delete()
        return HttpResponseRedirect("/")
    except Article.DoesNotExist:
        raise Http404()

@user_passes_test(lambda u: u.has_perm("lib.change_article"),login_url='/admin/')
@requires_csrf_token
def save(request,article_id):
    if not ('title' in request.POST and 'content' in request.POST):
        raise Http404()
    if not (request.POST['title'] and request.POST['content']):
        raise Http404()
    try:
        article_id=int(article_id)
    except ValueError:
        raise Http404()
    try:
        articles=Article.objects.get(tid=article_id)
        articles.title=request.POST['title']
        articles.content=request.POST['content']
        articles.save()
        return HttpResponseRedirect('/article/'+str(article_id))
    except Article.DoesNotExist:
        raise Http404()
def post_comment(request,article_id):
    p=request.POST
    try:
        article_id=int(article_id)
        article=Article.objects.get(tid=article_id)
    except ValueError,Article.DoesNotExist:
        return HttpResponse("Illegal Arguments")
    if not ('name' in p and 'email' in p and 'content' in p):
        return HttpResponse("Illegal Arguments")
    if not (p['name'] and p['email'] and p['content']):
        return HttpResponse("Illegal Arguments")
    if not email_re.match(p['email']):
        return HttpResponse("Illegal email")
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        uip=request.META.get('HTTP_X_FORWARDED_FOR').split(',')[-1].strip()
    else:
        uip=request.META.get('REMOTE_ADDR')
    c=Comment(content=p['content'],time_stamp=datetime.now(),author=p['name'],ip=uip,email=p['email'],tid=article_id)
    c.save()
    article.comments+=1
    article.save()
    return HttpResponseRedirect('/article/'+str(article_id))

@user_passes_test(lambda u: u.has_perm("lib.delete_comment"),login_url='/admin/')
def delete_comment(request,comment_id):
    try:
        comment_id=int(comment_id)
        comment=Comment.objects.get(cid=comment_id)
    except ValueError,Comment.DoesNotExist:
        return Http404()
    atid=comment.tid
    article=Article.objects.get(tid=atid)
    comment.delete()
    article.comments-=1
    article.save()
    return HttpResponseRedirect('/article/'+str(atid))
