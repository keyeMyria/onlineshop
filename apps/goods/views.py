#!/usr/bin/python env
# coding=utf-8


from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


from .models import Goods
from .serializers import GoodsSerializer
from .filters import GoodsFilter


# Create your views here.
# Custom Config Pagination
class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Goods List: 分页、搜索、过滤、排序
    """

    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_fields = ('name', 'shop_price')

    filter_class = GoodsFilter     # custom filter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'add_time')

    # def get_queryset(self):
    #     queryset = Goods.objects.all()
    #     price_min = self.request.query_params.get("price_min", 0)   # default value is 0
    #     if price_min:
    #         queryset = queryset.filter(shop_price__gt=int(price_min))   # gt greater than
    #     return queryset

