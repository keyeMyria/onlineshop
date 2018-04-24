#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/24 22:13'

import json
import requests

"""
个人开发者实测云片网功能极其不友好，非公司需要建议个人毋庸
个人开发者只能用测试
https://www.yunpian.com/doc/zh_CN/domestic/single_send.html
"""


class YunPian(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        params = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text":  "【云片网】您的验证码是{code}"
        }

        response = requests.post(self.single_send_url, data=params)

        re_dict = json.loads(response.text)

        print(re_dict)


if __name__ == '__main__':
    yun_pian = YunPian("your_api_key")
    yun_pian.send_sms("2017", "1355555555")

