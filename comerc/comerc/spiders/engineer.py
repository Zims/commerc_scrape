# -*- coding: utf-8 -*-
import scrapy
# import time
# the site is blocking me so I need to chose a new one

class EngineerSpider(scrapy.Spider):
    name = 'engineer'
    # allowed_domains = ['www.globalspec.com']
    page_letter = 'A'
    page_num = 1
    start_urls = [f'https://www.globalspec.com/SpecSearch/SuppliersByName/AllSuppliers/{page_letter}/{page_num}/']


    def parse(self, response):
        urls = response.css("td.name.selected-row > a::attr(href),td.name.grey-selected-row > a::attr(href)").extract()
        # print(f'Lenght of url list:{len(urls)}')
        # print(urls)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_details)

        # if page_num < 10:
        # time.sleep(10)

        # next_page = 'https://www.globalspec.com/SpecSearch/SuppliersByName/AllSuppliers/A/' + str(self.page_num) + '/'
        # print(f'______________________________{next_page}________________________________')

         # if self.page_num < 39:
            # self.page_num += 1
            # yield response.follow(next_page, self.parse)
   


    def parse_details(self, response):
        yield{
            'name': response.css("#supplier-info > h1::text").extract_first(),
            'website': response.css("#supplier-contact-info > div:nth-child(2) > a::attr(href)").extract_first()
        }

        