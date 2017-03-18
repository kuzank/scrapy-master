# !/usr/bin/python
# -*- coding: utf-8 -*-

from scrapy import Field
import scrapy


"""
WwwspiderItem是一个表示存储信息的类，当爬虫爬下html等信息是，
可以通过xpath、CSS、beautifulSoup等方式从html中提取信息，并将提取到的信息存放在声明好的item类中，


name = scrapy.Field()，声明之后的name可以存储string，数值，dict，列表或者元组等信息,
可以把name当成一个万能的存储载体就好了

"""

class WwwspiderItem(scrapy.Item):
    name = Field()
    age = Field()
    email = Field()
    phone = Field()


class DouBanItem(scrapy.Item):
    movie_url = Field()
    movie_picture = Field()
    title = Field()

    
class DoubanMailItem(scrapy.Item):
    sender_time = Field()     # 发送时间
    sender_from = Field()     # 发送人
    url = Field()             # 豆邮详细地址
    title = Field()           # 豆邮标题

