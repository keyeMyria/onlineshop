#!/usr/bin/python env
# coding=utf-8

"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
from django.views.static import serve

import xadmin
from MxShop.settings import MEDIA_ROOT
# from goods.views_base import GoodsListView
from goods.views import GoodsListViewSet, CategoryViewSet

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter


# Create a router and register our viewsets with it.
router = DefaultRouter()

# Config goods url
router.register(r'goods', GoodsListViewSet, base_name="goods")

# Config category url
router.register(r'categorys', CategoryViewSet, base_name="categorys")


# custom bind -- comment Because use router
# goods_list = GoodsListViewSet.as_view({
#     'get': 'list',
# })

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # goods list page
    # url(r'goods/$', GoodsListView.as_view(), name="good-list"),

    # rest framework docs
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'doc/', include_docs_urls(title="招财猫电商API")),

    url(r'^', include(router.urls)),
    # url(r'goods/$', goods_list, name="good-list"),    # because use router

]
