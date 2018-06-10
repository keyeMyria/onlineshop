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
from users.views import SmsCodeViewSet, UserViewset

from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer


schema_view = get_schema_view(title='招财猫电商Swagger API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

# Create a router and register our viewsets with it.
router = DefaultRouter()

# Config goods url
router.register(r'goods', GoodsListViewSet, base_name="goods")

# Config category url
router.register(r'categorys', CategoryViewSet, base_name="categorys")

# Config send sms url  -- can test by admin add sms_code
router.register(r'code', SmsCodeViewSet, base_name="code")     # will connect to frontend code，change key in settings

# Config user register
router.register(r'users', UserViewset, base_name="users")


# custom bind -- comment Because use router
# goods_list = GoodsListViewSet.as_view({
#     'get': 'list',
# })

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # goods list page
    # url(r'goods/$', GoodsListView.as_view(), name="good-list"),

    # django rest framework auth
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # drf自带的token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),

    # jwt的认证接口   配合vue的接口
    url(r'^login/', obtain_jwt_token, name="jwt_auth"),

    # drf自带的doc, DRF Built-in API docs and Generate schema with valid `request` instance
    url(r'^bi_docs/', include_docs_urls(title="招财猫电商API", public=False)),

    # swagger doc
    url(r'^swagger_docs/', schema_view, name="swagger_docs"),  # need to comfirm


    url(r'^', include(router.urls)),   # api在根目录，一般不会这样的
    # url(r'goods/$', goods_list, name="good-list"),    # because use router

]
