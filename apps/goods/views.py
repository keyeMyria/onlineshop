#!/usr/bin/python env
# coding=utf-8


from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend


from .models import Goods, GoodsCategory
from .serializers import GoodsSerializer, CategorySerializer
from .filters import GoodsFilter


# Create your views here.
# Custom Config Pagination
class GoodsPagination(PageNumberPagination):
    # page_size = 12
    # page_size_query_param = 'page_size'
    # page_query_param = 'page'
    # max_page_size = 100
    # 全局设置过的话一般不推荐局部再设置了，否则会报错
    pass


class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    Goods List: 分页、搜索、过滤、排序
    """

    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    # authentication_classes = (TokenAuthentication,)    # 一个要注意逗号，这里是公开页面，不能配置用户验证
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_fields = ('name', 'shop_price')

    filter_class = GoodsFilter     # custom filter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'shop_price')

    # def get_queryset(self):
    #     queryset = Goods.objects.all()
    #     price_min = self.request.query_params.get("price_min", 0)   # default value is 0
    #     if price_min:
    #         queryset = queryset.filter(shop_price__gt=int(price_min))   # gt greater than
    #     return queryset


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    retrieve:
        获取商品分类详情
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer

