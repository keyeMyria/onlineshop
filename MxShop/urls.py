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
from django.contrib import admin
from django.views.static import serve
from django.views.generic import TemplateView


import xadmin
from MxShop.settings import MEDIA_ROOT
# from goods.views_base import GoodsListView
from goods.views import GoodsListViewSet, CategoryViewSet
from users.views import SmsCodeViewSet, UserViewset
from user_operation.views import UserFavViewset

from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from rest_framework_swagger.views import get_swagger_view

from rest_framework_jwt.views import obtain_jwt_token

# from rest_framework.schemas import get_schema_view
# from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
# schema_view = get_schema_view(title='AICTF Swagger API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

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

# Config user collection favorite things
router.register(r'userfavs', UserFavViewset, base_name="userfavs")



# custom bind -- comment Because use router
# goods_list = GoodsListViewSet.as_view({
#     'get': 'list',
# })

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^xadmin/', xadmin.site.urls),

    url(r'^', include(router.urls)),   # api在根目录，一般不会这样的

    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # django rest framework auth
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # drf自带的token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),

    # jwt的认证接口   配合vue的接口
    url(r'^login/', obtain_jwt_token, name="jwt_auth"),

    # goods list page
    # url(r'goods/$', GoodsListView.as_view(), name="good-list"),

    # url(r'goods/$', goods_list, name="good-list"),    # because use router
#    url(r'^index/', TemplateView.as_view(template_name="index.html"), name="index"),

]

# config API docs
urlpatterns += [
    # drf自带的doc, DRF Built-in API docs and Generate schema with valid `request` instance
    # DRF docs, pip install coreapi
    url(r'^drf-docs/', include_docs_urls(title="AICTF DRF API", public=False)),

    # Swagger docs, pip install django-rest-swagger
    url(r'^swagger-docs/', get_swagger_view(title='Swagger API'))
]
