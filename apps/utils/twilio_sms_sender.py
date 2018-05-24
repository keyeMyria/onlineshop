#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/4/24 22:36'

from twilio.rest import Client


class TwilioSmsSender(object):

    def __init__(self, account_sid, auth_token):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.client = Client(account_sid, auth_token)

    def send_sms(self, receiver_num, sender_num, body):
        """
        sms_status["code"]  1 success , 0 failed
        :param receiver_num:
        :param sender_num:
        :param body:
        :return:
        """
        sms_status = dict()
        try:
            message = self.client.api.account.messages.create(to=receiver_num,  # 区号+你的手机号码
                                                              from_=sender_num,  # 你的 twilio 电话号码
                                                              body=body)
            print("send sms success: {}".format(message))
            sms_status["code"] = 1
            sms_status["msg"] = u"短信发送成功"
        except Exception as e:
            print("send sms failed: \n{}".format(e))
            sms_status["code"] = 0
            sms_status["msg"] = u"短信发送失败"

        return sms_status


if __name__ == '__main__':
    # filled in detail info
    tss = TwilioSmsSender("your_account_sid", "your_auth_token")
    tss.send_sms("receiver_num", "sender_num", "sms content")

    # https://note.youdao.com/web/#/file/7C77DF9BFF444BCCB879AB8CB75E70C3/note/WEB0264237a46a16520c91958a0f3daca2c/?search=twilio
