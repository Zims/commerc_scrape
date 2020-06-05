# -*- coding: utf-8 -*-
import scrapy


class YpDentistWaSpider(scrapy.Spider):
    name = 'yp_dentist_wa'
    # allowed_domains = ['www.yellowpages.com']
    start_urls = ['https://www.yellowpages.com/search?search_terms=dentist/']

    def parse(self, response):
        for company in response.xpath('//*[@class="result"]'):
            name = company.xpath('div/div/div/h2/a[@class="business-name"]/span/text()').extract_first()
            phone = company.xpath('//div/div/div/div/div[@class="phones phone primary"]/text()').extract_first()
            website = company.xpath('div/div/div/h2/a[@class="business-name"]/@href').extract_first()
            yield{'Name':name,'Phone':phone, 'Website':website}
            print(f'Name is _______________________{phone}')
            
                