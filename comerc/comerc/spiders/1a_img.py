import scrapy
from urllib.parse import urljoin


class A1aSpider(scrapy.Spider):
    name = '1a_img'
    allowed_domains = ['1a.lv']
    start_urls = ['https://www.1a.lv/c/datortehnika-preces-birojam/portativie-datori-un-aksesuari/portativie-datori/2t6?page_per=72&view_mode=grid']

    def parse(self, response):
        raw_image_urls = response.xpath('//img[@class="catalog-taxons-product__image"]/@src').getall()
        clean_img_urls = []
        for img_url in raw_image_urls:
            clean_img_urls.append(response.urljoin(img_url))

        yield {
            'image_urls': clean_img_urls
        }