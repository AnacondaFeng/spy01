# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['news.cnblogs.com']
    start_urls = ['http://news.cnblogs.com/']

    def parse(self, response):
        # '//*[@id="entry_654242"]/div[2]/h2/a'  getXPath
        # url = response.xpath('//*[@id="entry_654242"]/div[2]/h2/a/@href').extract_first("")
        # url = response.xpath('//div[@id="news_list"]/div[1]/div[2]/h2/a/@href').extract_first("")
        # 这种做法最标准
        url = response.xpath('//div[@id="news_list"]//h2[@class="news_entry"]/a/@href').extract()
        pass


