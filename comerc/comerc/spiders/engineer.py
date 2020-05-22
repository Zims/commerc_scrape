# -*- coding: utf-8 -*-
import scrapy


class EngineerSpider(scrapy.Spider):
    name = 'engineer'
    allowed_domains = ['www.globalspec.com']
    start_urls = ['https://www.globalspec.com/SpecSearch/SuppliersByName/AllSuppliers/A/1/']


    def parse(self, response):

        urls = response.css("td.name.selected-row > a::attr(href)").extract()
        print(f'I got theese urls______________________________________________________________________________:{urls}')
        for url in urls:
            yield print(url) 
            scrapy.Request(url=urls, callback=self.parse_details)
            # yield {
                # 'name': item.xpath(".//a/text()").get(),
                # 'Link': item.xpath(".//a/@href").get()
            # }
        # pass
        # print(response.body)
        # //tr[contains(@class, 'result-item')]
    def parse_details(self, response):
        yield{
            'name': response.xpath("//div[@id='supplier-info']/h1[@class='info-section supplier-name no-icons basic-listing']/text()").get(),
            'web': response.xpath("//a[@class='icon-accompanying-link blue-arrow-left']/@href").get()
        }
