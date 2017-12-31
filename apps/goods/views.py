#!/usr/bin/python env
# coding=utf-8


from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import Goods
from .serializers import GoodsSerializer


# Create your views here.
# Custom Config Pagination
class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class GoodsListView(generics.ListAPIView):
    """
    Goods List
    """

    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination

