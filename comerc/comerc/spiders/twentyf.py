# -*- coding: utf-8 -*-
import scrapy


class TwentyfSpider(scrapy.Spider):
    name = 'twentyf'
    allowed_domains = ['24.lv']
    start_urls = [
        'https://24.lv/datoru-un-biroja-tehnika-en/portatvie-datori-un-piederumi/portatvie-datori/']

    def parse(self, response):
        for product in response.xpath("//div[@class='col-tile']"):
            yield{
                'name': product.xpath(".//a[@class='product-title']/text()").get(),
                'price': product.xpath('.//*[@class="ty-price-num"][2]/text()').get()


            }
            

            # yield{
            #     'title': product.xpath(".//div[@class='specs-wrap']//div[@class='specs js-item-specs']/h3[@class='js-item-title']/text()").get(),
            #     'price': product.xpath(".//div[@class='specs-wrap']//div[@class='specs js-item-specs']/div[@class=' price']/text()").get()

            # }
