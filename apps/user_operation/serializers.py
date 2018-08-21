#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/8/22 00:02'

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from user_operation.models import UserFav


class UserFavSerializer(serializers.ModelSerializer):
    # 自动获取user为当前登陆用户
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav
        fields = ("user", "goods", "id")  # cancel collect favorite need id

        # validators可以作用在某个字段，也可以写在meta中
        validators = [
            UniqueTogetherValidator(queryset=UserFav.objects.all(), fields=("user", "goods"), message="已经收藏")
        ]
