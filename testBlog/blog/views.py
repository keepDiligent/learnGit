from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import Http404
from django.views.generic.dates import MonthArchiveView
from django.db.models import Count


# Create your views here.
def homePage(request):
 try:
  articleList=Article.objects.all()
 except Article.DoesNotExists:
  raise Http404

 paginator=Paginator(articleList,3)
 page=request.GET.get('page')
 numPages=range(1,paginator.num_pages+1)
 try:
  articleList=paginator.page(page)
 except PageNotAnInteger:
  articleList=paginator.page(1)
 except EmptyPage:
  articleList=paginator.page(numPages)

 archives = Article.objects.all().extra(select={'year':"strftime('%Y',publish_time)",'month':"strftime('%m',publish_time)"}).values('year','month').annotate(Count('id')).order_by('-year','-month')
 context={
      'articleList':articleList,
      'numPages':numPages,
      'archives':archives,
 }


 return render(request,'blog/homePage.html',context)


def articleList(request):
 try:
  articleList = Article.objects.all()
 except Article.DoesNotExists:
  raise Http404
 return render(request,'blog/catalog.html',{'articleList':articleList})
 
 
def article(request,id):
 try:
  article=Article.objects.get(id=str(id))
 except Article.DoesNotExists:
  raise Http404
 return render(request,'blog/article.html',{'article':article}) 

class ArticleMonthArchiveView(MonthArchiveView):
	model = Article
	date_field = 'publish_time'
	month_format = '%m'
	template_name = 'blog/artice_archive_month.html'
	queryset = Article.objects.all()

