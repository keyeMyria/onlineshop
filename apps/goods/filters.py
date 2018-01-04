#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '18/1/4 16:50'


import django_filters
from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品大的过滤类
    """
    price_min = django_filters.NumberFilter(name="shop_price", lookup_expr='gte')   # 大于等于
    price_max = django_filters.NumberFilter(name="shop_price", lookup_expr='lte')
    name = django_filters.CharFilter(name="name", lookup_expr='icontains')  # 模糊查询'contains'类似sql like, 忽略大小写加i
    # name = django_filters.CharFilter(name="name")   # 完全匹配

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max', 'name']