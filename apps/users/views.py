#!/usr/bin/env python
# -*- coding:utf-8 -*-

from random import choice

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets, status
from rest_framework.response import Response

from users.models import VerifyCode
from users.serializers import SmsSerializer, UserRegSerializer
from utils.twilio_sms_sender import TwilioSmsSender
from MxShop.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_SENDER_NUM


User = get_user_model()       # get settings.AUTH_USER_MODEL


class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    # 要继承自ModelBackend
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username)|Q(mobile=username)|Q(email=username))   # add support e-mail addr login
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class SmsCodeViewSet(CreateModelMixin, viewsets.GenericViewSet):
    """
    发送短信验证码
    """
    serializer_class = SmsSerializer

    def generate_code(self):
        """
        生成4位数字验证码
        :return:
        """
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))   # 从seeds里面随机取1个数字加入random_str

        return "".join(random_str)    # 把list join成字符串

    # use CreateModelMixin create()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)    # failed will return 400

        mobile = serializer.validated_data["mobile"]
        receiver_num = "+86" + mobile
        print(receiver_num)   # "13xxxxx"  need add +86

        code = self.generate_code()
        sms_content = "[FSPT] Your verify code is {}".format(code)
        tss = TwilioSmsSender(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        sms_status = tss.send_sms(receiver_num, TWILIO_SENDER_NUM, sms_content)

        if sms_status["code"] != 1:   # sms_status["code"]  1 success , 0 failed
            return Response({
                "mobile": sms_status["msg"]
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            # 短信发送成功后才保存到数据库
            code_record = VerifyCode(code=code, mobile=mobile)
            code_record.save()

            return Response({
                "mobile": mobile
            }, status=status.HTTP_201_CREATED)


class UserViewset(CreateModelMixin, viewsets.GenericViewSet):
    """
    User
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()
