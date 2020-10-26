# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin


class A1aSpider(scrapy.Spider):
    name = '1a'
    allowed_domains = ['1a.lv']
    start_urls = ['https://www.1a.lv/c/datortehnika-preces-birojam/portativie-datori-un-aksesuari/portativie-datori/2t6?page_per=72&view_mode=grid']

    def parse(self, response):
        for product in response.xpath("//div[@class='catalog-taxons-product__hover']"):
            yield{
                'name': product.xpath("normalize-space(.//a[@class='catalog-taxons-product__name']/text())").get(),
                'price': product.xpath("normalize-space(.//span[@class='catalog-taxons-product-price__item-price']/span[1]/text())").get(),
                }
        part_url = response.xpath("//a[@class='next ']/@href").get()
        url = response.urljoin(part_url)

    # print(f'Returned url: {url}')
        yield scrapy.Request(url, callback=self.parse)
