#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/28 12:14'

from rest_framework import serializers

from goods.models import Goods, GoodsCategory, GoodsImage


class CategorySerializer3(serializers.ModelSerializer):
    """
        商品类别序列化  三级目录
    """
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    """
        商品类别序列化  二级目录
    """
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
        商品类别序列化
    """
    sub_cat = CategorySerializer2(many=True)    # 可能有多个二类目录

    class Meta:
        model = GoodsCategory
        fields = "__all__"


# 如何序列化外键
class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ("image",)


class GoodsSerializer(serializers.ModelSerializer):

    category = CategorySerializer()
    images = GoodsImageSerializer(many=True)    # Goods可能取到多个images

    class Meta:
        model = Goods
        # fields = ('name', 'click_num', 'market_price', 'add_time')
        # get all fields
        fields = "__all__"






