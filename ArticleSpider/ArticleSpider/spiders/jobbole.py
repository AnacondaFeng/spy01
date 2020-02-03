# -*- coding: utf-8 -*-

from urllib import parse

# from scrapy import Selector
import scrapy
from scrapy import Request


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['news.cnblogs.com']
    start_urls = ['http://news.cnblogs.com/']

    def parse(self, response):
        """
        1.获取新闻url交给下载器进行下载并调用相应解析方法
        2.获取下一页url交给scrapy下载，完成后交给parse继续跟进
        :param response:
        :return:
        """
        # '//*[@id="entry_654242"]/div[2]/h2/a'  getXPath
        # url = response.xpath('//*[@id="entry_654242"]/div[2]/h2/a/@href').extract_first("")
        # url = response.xpath('//div[@id="news_list"]/div[1]/div[2]/h2/a/@href').extract_first("")
        # sel = Selector(text=response.text)

        # 这种做法最标准xpath
        # url = response.xpath('//div[@id="news_list"]//h2[@class="news_entry"]/a/@href').extract()

        # css选择器
        # urls = response.css('div#news_list h2 a::attr(href)').extract()
        post_nodes = response.css('#news_list .news_block')

        for post_node in post_nodes:
            image_url = post_node.css('.entry_summary a img::attr(href)').extract_first("")
            post_url = post_node.css('h2 a::attr(href)').extract_first("")
            yield Request(url=parse.urljoin(response.url, post_url),  # yield作用 获得一个处理一个
                          meta={"front_image_url": image_url}, callback=self.parse_detail)

        #     提取下一页url发送scrapy处理
        # css方式
        # next_url = response.css("div.pager a:last-child::text").extract_first("")

        # if next_url == "Next >":
        #     next_url = response.css("div.pager a:last-child::attr(href)").extract_first("")
        #     yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse())

        # xpath方式
        next_url = response.xpath("//a[contains(text(), 'Next >')]/@href").extract_first("")
        yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse())

    def parse_detail(self, response):
        pass
