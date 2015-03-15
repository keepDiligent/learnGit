from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import Http404

# Create your views here.
def homePage(request):
 try:
  articleList=Article.objects.all().order_by('-publish_time')
 except Article.DoesNotExists:
  raise Http404
 paginator=Paginator(articleList,3)
 page=request.GET.get('page')
 try:
  articleList=paginator.page(page)
 except PageNotAnInteger:
  articleList=paginator.page(1)
 except EmptyPage:
  articleList=paginator.page(paginator.num_pages)
 return render(request,'blog/homePage.html',{'articleList':articleList})
def articleList(request):
 try:
  articleList = Article.objects.all().order_by('-publish_time')
 except ArticleDoesNotExists:
  raise Http404
 return render(request,'blog/catalog.html',{'articleList':articleList})
def article(request,id):
 try:
  article=Article.objects.get(id=str(id))
 except ArticleDoesNotExists:
  raise Http404
 return render(request,'blog/article.html',{'article':article}) 
