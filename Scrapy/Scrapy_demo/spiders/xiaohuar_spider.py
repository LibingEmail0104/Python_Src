#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy

class XiaoHuaSpider (scrapy.spiders.Spider):
    name = "xiaohuar"
    allowed_domains = ["xiaohuar.com"]
    start_urls=[
        "http://www.xiaohuar.com/hua/"
    ]

