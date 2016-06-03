# -*- coding: utf-8 -*-


from django.conf.urls import url
from django.contrib import admin
from .views import NewsView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', NewsView.as_view(), name="detail"),
    url(r'^(?P<news_id>\d+)/$', 'news.views.show_news'),
    url(r'^(?P<news_id>\d+)/like/$', 'news.views.show_news'),
]
