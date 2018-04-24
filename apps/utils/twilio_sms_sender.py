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
        message = self.client.api.account.messages.create(to=receiver_num,  # 区号+你的手机号码
                                                          from_=sender_num,  # 你的 twilio 电话号码
                                                          body=body)
        # print(message)


if __name__ == '__main__':
    # filled in detail info
    tss = TwilioSmsSender("your_account_sid", "your_auth_token")
    tss.send_sms("receiver_num", "sender_num", "sms content")
