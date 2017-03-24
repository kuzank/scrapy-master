#!/usr/bin/env python
# -*- coding:utf-8 -*-

from scrapy import cmdline
import scrapy
from scrapy_splash import SplashRequest

"""
前提：
    安装scrapy-splash：pip install scrapy-splash
提醒：
    不要滥用scrapy-splash，能不用就不用
    除非异步加载数据真真的很难解析，不然不要用渲染，这是终极武器

有些网页数据是通过异步加载完成的，通过抓包分析和提取一般可以解析到这些数据
但是也有一些数据是用dwr传送的，
例如http://study.163.com/course/introduction/1455026.htm#/courseDetail，在通过对这个页面进行抓包
在抓包文件http://study.163.com/dwr/call/plaincall/PlanNewBean.getPlanCourseDetail.dwr?1490328841060中
你会发现这些异步数据很难去解析
还有很多无法解析的情况

这个时候我们就可以使用scrapy-splash进行页面渲染，再去解析数据
"""

class DownloadHtml(scrapy.Spider):
    name = "demo6"
    allowed_domains = ["www.example.com", ]
    start_urls = ["http://www.example.com", ]
    HEADERS = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, sdch, br',
        'accept-language': 'zh-CN,zh;q=0.8',
    }

    def parse(self, response):
        """
        :url是你要使用scrapy-splash进行渲染的URL地址
        """
        url = 'http://www.example.com'
        # wait是scrapy-splash渲染页面的时间
        yield SplashRequest(url,self.splash_parse, args={'wait': 0.5, })


    def splash_parse(self, response):
        print response
        print response.body


if __name__ == '__main__':
    scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'demo6'])

