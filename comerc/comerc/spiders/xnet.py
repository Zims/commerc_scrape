# -*- coding: utf-8 -*-
import scrapy


class XnetSpider(scrapy.Spider):
    name = 'xnet'
    allowed_domains = ['www.xnet.lv/lv/elektronika/portativie-datori/portativie-datori']
    start_urls = ['http://www.xnet.lv/lv/elektronika/portativie-datori/portativie-datori/']

    def parse(self, response):
        pass
