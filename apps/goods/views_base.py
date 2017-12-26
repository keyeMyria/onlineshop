#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = 'TesterCC'
# __time__   = '17/12/27 04:40'

from django.views.generic.base import View

from goods.models import Goods


class GoodsListView(View):
    def get(self, request):
        """
        通过Django的view实现商品列表页
        :param request:
        :return:
        """
        json_list = []
        goods = Goods.objects.all()[:10]     # 不获取全部，以防加载过慢
        for good in goods:
            json_dict = {}
            json_dict["name"] = good.name
            json_dict["category"] = good.category.name
            json_dict["market_price"] = good.market_price
            json_list.append(json_dict)

        # return json data
        from django.http import HttpResponse
        import json
        return HttpResponse(json.dumps(json_list), content_type="application/json")