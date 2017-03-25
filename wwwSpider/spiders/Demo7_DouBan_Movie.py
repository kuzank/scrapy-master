#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy
import random
import json
import urllib
from scrapy import cmdline
from wwwSpider.util.header import User_Agent_Lists

class DownloadHtml(scrapy.Spider):
    name = "demo7"
    # allowed_domains = ["study.163.com", ]
    # start_urls = ["http://study.163.com", ]
    get_video_info = 'https://movie.douban.com/j/search_subjects?type=movie&tag=TAG&sort=recommend&page_limit=20&page_start=0'
    HEADERS = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, sdch, br',
        'accept-language': 'zh-CN,zh;q=0.8',
        'refer': 'https://movie.douban.com',
        'user-agent':random.choice(User_Agent_Lists)
    }

    def start_requests(self):
        url = 'https://movie.douban.com/j/search_tags?type=movie&tag=%E7%83%AD%E9%97%A8'
        yield scrapy.Request(url=url,callback=self.tag_parse,headers=self.HEADERS)

    def tag_parse(self, response):
        print '豆瓣电影分类：' + response.body
        body = json.loads(response.body)
        for tag in body['tags']:
            # print tag,urllib.quote(tag.encode('utf-8'))
            video_info_url = self.get_video_info.replace('TAG',urllib.quote(tag.encode('utf-8')))
            yield scrapy.Request(url=video_info_url,callback=self.print_parse,headers=self.HEADERS)

    def print_parse(self, response):
        print response.body


if __name__ == '__main__':
    scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'demo7'])




