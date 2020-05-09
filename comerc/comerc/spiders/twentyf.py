# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin


class TwentyfSpider(scrapy.Spider):
    name = 'twentyf'
    allowed_domains = ['24.lv']
    start_urls = [
        'https://24.lv/datoru-un-biroja-tehnika-en/portatvie-datori-un-piederumi/portatvie-datori/page-10/']

    def parse(self, response):
        for product in response.xpath("//div[@class='col-tile']"):
            yield{
                'name': product.xpath(".//a[@class='product-title']/text()").get(),
                'price': product.xpath('.//*[@class="ty-price-num"][2]/text()').get()
            }
            url = response.xpath("(//div[@class='ty-pagination']/a/@href)").get()
            # url = response.urljoin(next_page_partial_url)

            print(f'Returned url: {url}')
            yield scrapy.Request(url, callback=self.parse)
            # # yield{
            #     'title': product.xpath(".//div[@class='specs-wrap']//div[@class='specs js-item-specs']/h3[@class='js-item-title']/text()").get(),
            #     'price': product.xpath(".//div[@class='specs-wrap']//div[@class='specs js-item-specs']/div[@class=' price']/text()").get()

            # }
