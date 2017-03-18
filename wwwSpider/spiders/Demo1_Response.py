#!/usr/bin/python
# -*- coding: UTF-8 -*-

import scrapy
from scrapy import cmdline

class Scrapy_Demo(scrapy.Spider):
    name = 'demo1'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com']


    def parse(self, response):
        print 'url----' + str(response.url)
        print 'headers----' + str(response.headers)
        print 'body----' + str(response.body)
        print 'status----' + str(response.status)
        print 'meta----' + str(response.meta)
        print 'flags----' + str(response.flags)



        
if __name__ == '__main__':
    scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'demo1'])
