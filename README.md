    Scrapy Demo For Learning

    scrapy框架的知识

    Scrapy，Python开发的一个快速,高层次的屏幕抓取和web抓取框架，用于抓取web站点并从页面中提取结构化的数据。
    Scrapy用途广泛，可以用于数据挖掘、监测和自动化测试。
    Scrapy吸引人的地方在于它是一个框架，任何人都可以根据需求方便的修改。
    它也提供了多种类型爬虫的基类，如BaseSpider、sitemap爬虫等，最新版本又提供了web2.0爬虫的支持。



    spider在爬取网页的时候要分析网页的内容，并且从网页中提取有用的内容，这些内容就可以存放在item中，
    通过return item 或者 yield item 就可以把整个item的内容传递到pipeline，
    这个时候就可以在pipeline中写代码，把item的内容进行处理，比如删除重复的内容，或者把item存放到数据库中


