#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/5/24 22:09'


import re
from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from MxShop.settings import REGEX_MOBILE
from users.models import VerifyCode

User = get_user_model()


class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        """
        验证手机号
        :param mobile:
        :return:
        """

        # 手机是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("用户已存在")

        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码不合法")

        # 验证发送频率
        one_minute_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_minute_ago, mobile=mobile):
            raise serializers.ValidationError("距离上一次发送未超过60s")

        return mobile


class UserRegSerializer(serializers.ModelSerializer):
    code = serializers.CharField(required=True, max_length=4, write_only=True, min_length=4, label="验证码",
                                 error_messages={
                                     'blank': '请输入验证码',
                                     'required': '请输入验证码',
                                     'max_length': '验证码格式错误',
                                     'minx_length': '验证码格式错误',
                                 }, help_text='验证码')   # 添加的字段
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])
    password = serializers.CharField(
        label="密码", write_only=True,
        style={'input_type': 'password'}
    )

    def create(self, validated_data):
        """
        重载create method  另一种方法是利用django信号量Signals的机制
        :param validated_data:
        :return:
        """
        user = super(UserRegSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def validate_code(self, code):
        # 如果使用get，需要try except
        # try:
        #     verify_records = VerifyCode.objects.get(mobile=self.initial_data["username"]).order_by("-add_time")
        # except VerifyCode.DoesNotExist as e:
        #     # 最好加上错误日志打印
        #     pass
        # except VerifyCode.MultipleObjectsReturned as e:
        #     pass

        # 验证验证码是否存在于数据库
        verify_records = VerifyCode.objects.filter(mobile=self.initial_data["username"]).order_by("-add_time")   # initial_data, from front_end post

        if verify_records:
            last_record = verify_records[0]

            five_minute_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)   # 有效期5分钟

            if five_minute_ago > last_record.add_time:
                raise serializers.ValidationError("验证码过期")

            if last_record.code != code:
                raise serializers.ValidationError("验证码错误")

        else:

            raise serializers.ValidationError("验证码错误")

    def validate(self, attrs):
        attrs['mobile'] = attrs['username']
        del attrs['code']
        return attrs

    class Meta:
        model = User
        fields = ("username", "mobile", "code", "password")       # UserProfile继承的是django自带的字段










