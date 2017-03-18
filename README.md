# scrapy-master
Scrapy Demo For Learning


scrapy框架的知识


spider在爬取网页的时候要分析网页的内容，并且从网页中提取有用的内容，这些内容就可以存放在item中，
通过return item 或者 yield item 就可以把整个item的内容传递到pipeline，
这个时候就可以在pipeline中写代码，把item的内容进行处理，比如删除重复的内容，或者把item存放到数据库中


