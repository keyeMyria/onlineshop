#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Goods


# Create your models here.

User = get_user_model()


class UserFav(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(User, verbose_name="用户")
    goods = models.ForeignKey(Goods, verbose_name="商品")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.name


class UserLeavingMessage(models.Model):
    """
    用户留言  3-5  02:30
    """
    pass



