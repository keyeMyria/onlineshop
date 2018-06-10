#!/usr/bin/env python
# encoding: utf-8

from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = "用户管理"

    def ready(self):
        """
        for use signals
        """
        import users.signals