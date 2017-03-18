#!/usr/bin/python
# -*- coding: UTF-8 -*-

import scrapy
from scrapy import cmdline
from scrapy import Request
from wwwSpider.util.header import CommonHeader
from wwwSpider.items import DouBanItem

class Scrapy_Demo(scrapy.Spider):
    name = 'demo3'
    #allowed_domains = ['']


    def start_requests(self):
        url = 'https://movie.douban.com/review/best/?qq-pf-to=pcqq.group'
        CommonHeader['Referer'] = 'https://movie.douban.com/'
        yield Request(url=url,callback=self.parse,headers=CommonHeader)


    def parse(self, response):
        print '-------------------------------------------------------------'
        sels = response.xpath('//div[@class="review-list chart"]/div')
        douBanItem = DouBanItem()
        for sel in sels:
            #print sel.extract()
            douBanItem['movie_url'] = sel.xpath('div/a/@href').extract()[0]
            douBanItem['movie_picture'] = sel.xpath('div/a/img/@src').extract()[0]
            douBanItem['title'] = sel.xpath('div/header/h3/a/text()').extract()[0]

            print douBanItem
            yield douBanItem
            # or return douBanItem



if __name__ == '__main__':
    scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'demo3'])
