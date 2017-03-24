#!/usr/bin/env python
# -*- coding:utf-8 -*-

from scrapy import cmdline
import scrapy
import json

"""
FormRequest做用户登录
这个是知乎的验证登录，没有做成功
这里需要的图片验证还没有完成
"""

class ZhihuSpider(scrapy.Spider):
    name = "demo4"
    allowed_domains = ["www.zhihu.com"]
    headers = {
            'Host': 'www.zhihu.com',
            'Referer': 'http://www.zhihu.com',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
        }

    def start_requests(self):
        return [scrapy.Request('http://www.zhihu.com/#signin', callback=self.zhihu_login)]


    def zhihu_login(self, response):
        _xsrf = response.xpath(".//*[@id='sign-form-1']/input[2]/@value").extract()[0]
        return [scrapy.FormRequest(
                url = 'http://www.zhihu.com/login/email',    # 这是post的真实地址
                formdata={'_xsrf': _xsrf,
                    'account': '15219378950',    # email
                    'password': 'tobestudy520',    # password
                    'remember_me': 'true',
                },
                headers=self.headers,
                callback=self.page_content,
        )]


    def page_content(self, response):
        with open('e://first_page.html', 'wb') as f:
            f.write(response.body)
        print response.body
        print u'\u9a8c\u8bc1\u7801\u9519\u8bef'



if __name__ == '__main__':
    cmdline.execute(argv=['scrapy', 'crawl', 'demo4'])


