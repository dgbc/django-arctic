# -*-*- encoding: utf-8 -*-*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from articles.views import (
    ArticleListView, ArticleCreateView,
    ArticleUpdateView, ArticleDeleteView,
    CategoryListView, CategoryCreateView,
    CategoryUpdateView, CategoryDeleteView,
    CategoryArticlesListView, TagListView,
    TagCreateView, TagUpdateView, TagDeleteView
)
from dashboard.views import DashboardView
from users.views import LoginView


article_patterns = [
    url(r'^$', ArticleListView.as_view(), name='list'),
    url(r'^create/$', ArticleCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', ArticleUpdateView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/delete/$', ArticleDeleteView.as_view(), name='delete'),
    url(r'^category/$', CategoryListView.as_view(), name='category-list'),
    url(r'^category/create/$', CategoryCreateView.as_view(), name='category-create'),
    url(r'^category/(?P<pk>\d+)/$', CategoryUpdateView.as_view(), name='category-detail'),
    url(r'^category/articles/(?P<pk>\d+)/$', CategoryArticlesListView.as_view(), name='category-articles-list'),
    url(r'^category/(?P<pk>\d+)/delete/$', CategoryDeleteView.as_view(), name='category-delete'),
    url(r'^tags/$', TagListView.as_view(), name='tag-list'),
    url(r'^tags/create/$', TagCreateView.as_view(), name='tag-create'),
    url(r'^tags/(?P<pk>\d+)/$', TagUpdateView.as_view(), name='tag-detail'),
    url(r'^tags/(?P<pk>\d+)/delete/$', TagDeleteView.as_view(), name='tag-delete'),
]

urlpatterns = [
    url(r'^$', DashboardView.as_view(), name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^articles/', include(article_patterns, namespace='articles')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
