# -*- coding: utf-8 -*-
import scrapy


class XnetSpider(scrapy.Spider):
    name = 'xnet'
    allowed_domains = ['xnet.lv']
    start_urls = [
        'https://www.xnet.lv/lv/elektronika/portativie-datori/portativie-datori/?page=5&perpage=81']

    def parse(self, response):
        for product in response.xpath("//a[@class='thumbnail']"):

            yield{
                'title': product.xpath(".//div[@class='specs-wrap']//div[@class='specs js-item-specs']/h3[@class='js-item-title']/text()").get(),
                'price': product.xpath(".//div[@class='specs-wrap']//div[@class='specs js-item-specs']/div[@class=' price']/text()").get()

            }
            # 'url': product.xpath(".//div[@class='td_module_1 td_module_wrap td-animation-stack']/h3[@class='entry-title td-module-title']/a/@href").get(),

            # next_partial_url = response.xpath(".//ul[@class='pagination']/li[@class]/a[@class='setPage']/@href")[2].extract()
            # # full_url = 
            # print(f'I got the response: {next_partial_url}')
    #         yield scrapy.Request(next_page_url, callback=self.parse)
