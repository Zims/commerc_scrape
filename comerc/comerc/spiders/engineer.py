# -*- coding: utf-8 -*-
import scrapy


class EngineerSpider(scrapy.Spider):
    name = 'engineer'
    allowed_domains = ['www.globalspec.com']
    start_urls = ['https://www.globalspec.com/SpecSearch/SuppliersByName/AllSuppliers/A/1/']


    def parse(self, response):
        urls = response.css("td.name.selected-row > a::attr(href)").extract()
        print(urls)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_details)

    def parse_details(self, response):
        yield{
            'name': response.css("#supplier-info > h1::text").extract_first(),
            'website': response.css("#supplier-contact-info > div:nth-child(2) > a::attr(href)").extract_first()
        }
