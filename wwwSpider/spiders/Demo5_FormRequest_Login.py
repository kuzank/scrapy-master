#!/usr/bin/python
# -*- coding: UTF-8 -*-

import scrapy
import random
from scrapy import cmdline
from scrapy import FormRequest
from scrapy import Request
from wwwSpider.util.header import User_Agent_Lists

class Scrapy_Demo(scrapy.Spider):
    name = 'demo5'
    #allowed_domains = ['']
    Header = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'accounts.douban.com',
        'Origin': 'https://www.douban.com',
        'Referer': 'https://www.douban.com',
        'user-agent': random.choice(User_Agent_Lists),
    }

    def start_requests(self):
        yield Request(url='https://www.douban.com',
                    callback=self.douBan_login, headers=self.Header,meta={'cookiejar': 1})

    def douBan_login(self,response):
        yield FormRequest.from_response(
                url="https://accounts.douban.com/login",headers=self.Header,
                meta={'cookiejar': response.meta['cookiejar']},callback=self.after_login1,
                formdata={'form_email':'15219378950','form_password':'tobestudy520','login': u'登录'},
        )

    def after_login1(self,response):
        yield Request(url='https://www.douban.com/accounts/login?redir=https%3A//accounts.douban.com/',
                      callback=self.after_login2,headers=self.Header,meta={'cookiejar': response.meta['cookiejar']})

    def after_login2(self, response):
        yield FormRequest.from_response(
            url="https://accounts.douban.com/login", headers=self.Header,
            meta={'cookiejar': response.meta['cookiejar']}, callback=self.parse,
            formdata={'form_email': '', 'form_password': ''},
        )

    def parse(self, response):
        with open('e://douban.txt','w') as f:
            f.write(response.body)
        name = response.xpath('//a[@target="_blank"]/span/text()').extract()
        print name
        if len(name) > 0:
            print "Your DouBan Name Is : " + name





if __name__ == '__main__':
    scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'demo5'])
