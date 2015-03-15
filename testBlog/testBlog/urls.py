from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testBlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^homePage/$','blog.views.homePage',name='homePage'),
    url(r'^catalog/$','blog.views.articleList',name='articleList'),
    url(r'^article/(?P<id>\d+)/$','blog.views.article',name='article'),

)
