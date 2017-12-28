#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/28 12:14'

from rest_framework import serializers


class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, max_length=100)
    click_num = serializers.IntegerField(default=0)
    goods_front_image = serializers.ImageField()
