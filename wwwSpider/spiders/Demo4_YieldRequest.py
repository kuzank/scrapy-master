#!/usr/bin/python
# -*- coding: UTF-8 -*-

import scrapy
from scrapy import cmdline
from scrapy import Request
from wwwSpider.util.header import CommonHeader

class Scrapy_Demo(scrapy.Spider):
    name = 'demo4'
    #allowed_domains = ['']


    def start_requests(self):
        url = 'https://movie.douban.com/review/best/?qq-pf-to=pcqq.group'
        CommonHeader['Referer'] = 'https://movie.douban.com/'
        yield Request(url=url,callback=self.parse,headers=CommonHeader)


    def parse(self, response):
        """
        通过“后页”标签迭代所有的页面
        """
        sels = response.xpath('//span[@class="next"]/a/@href').extract()
        for sel in sels:
            next_url = response.urljoin(sel)
            print next_url
            yield Request(url=next_url,callback=self.parse,headers=CommonHeader)


            

if __name__ == '__main__':
    scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'demo4'])
