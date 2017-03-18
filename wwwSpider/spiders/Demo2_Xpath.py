#!/usr/bin/python
# -*- coding: UTF-8 -*-

import scrapy
from scrapy import cmdline
from scrapy import Request
from wwwSpider.util.header import CommonHeader

class Scrapy_Demo(scrapy.Spider):
    name = 'demo2'
    #allowed_domains = ['']


    def start_requests(self):
        url = 'https://movie.douban.com/review/best/?qq-pf-to=pcqq.group'
        CommonHeader['Referer'] = 'https://movie.douban.com/'
        yield Request(url=url,callback=self.parse,headers=CommonHeader,
                      # 不允许网页重定向
                      meta={'dont_redirect': True,'handle_httpstatus_list': [302]},)


    def parse(self, response):
        sels = response.xpath('//div[@class="review-list chart"]/div')
        for sel in sels:
            #print sel.extract()
            print '----------------------------------------------------------------'
            print 'movie_url----' + sel.xpath('div/a/@href').extract()[0]
            print 'movie_picture----' + sel.xpath('div/a/img/@src').extract()[0]
            print 'title----' + sel.xpath('div/header/h3/a/text()').extract()[0]


        print '---stop------'



        
if __name__ == '__main__':
    scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'demo2'])
