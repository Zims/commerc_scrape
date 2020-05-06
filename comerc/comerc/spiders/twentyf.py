# -*- coding: utf-8 -*-
import scrapy


class TwentyfSpider(scrapy.Spider):
    name = 'twentyf'
    allowed_domains = ['24.lv']
    start_urls = ['https://24.lv/datoru-un-biroja-tehnika-en/portatvie-datori-un-piederumi/portatvie-datori/']

    def parse(self, response):
        pass
