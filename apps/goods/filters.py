#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '18/1/4 16:50'


import django_filters
from django.db.models import Q
from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品大的过滤类
    """
    pricemin = django_filters.NumberFilter(name="shop_price", lookup_expr='gte')   # 大于等于
    pricemax = django_filters.NumberFilter(name="shop_price", lookup_expr='lte')
    name = django_filters.CharFilter(name="name", lookup_expr='icontains')  # 模糊查询'contains'类似sql like, 忽略大小写加i
    # name = django_filters.CharFilter(name="name")   # 完全匹配

    top_category = django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value)|Q(category__parent_category_id=value)|Q(category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax', 'name']
