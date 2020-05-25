# -*- coding: utf-8 -*-
import scrapy


class EngineerSpider(scrapy.Spider):
    name = 'engineer'
    # allowed_domains = ['www.globalspec.com']

    page_num = 1
    start_urls = ['https://www.globalspec.com/SpecSearch/SuppliersByName/AllSuppliers/A/1']


    def parse(self, response):
        urls = response.css("td.name.selected-row > a::attr(href),td.name.grey-selected-row > a::attr(href)").extract()
        # print(f'Lenght of url list:{len(urls)}')
        # print(urls)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_details)
        # if page_num < 10:

        next_page = 'https://www.globalspec.com/SpecSearch/SuppliersByName/AllSuppliers/A/' + str(self.page_num)
        if self.page_num < 39:
            self.page_num += 1
            yield response.follow(next_page, self.parse)


    def parse_details(self, response):
        yield{
            'name': response.css("#supplier-info > h1::text").extract_first(),
            'website': response.css("#supplier-contact-info > div:nth-child(2) > a::attr(href)").extract_first()
        }

        