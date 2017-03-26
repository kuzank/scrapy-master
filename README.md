    In This Project,We Talking About Scrapy Demo Which Was Using For Learning.

    About Scrapy Frame：
        Scrapy是Python开发的一个快速,高层次的屏幕抓取和web抓取框架，用于抓取web站点并从页面中提取结构化的数据。
        Scrapy用途广泛，可以用于数据挖掘、监测和自动化测试。
        Scrapy吸引人的地方在于它是一个框架，任何人都可以根据需求方便的修改。
        它也提供了多种类型爬虫的基类，如BaseSpider、sitemap爬虫等，最新版本又提供了web2.0爬虫的支持。 
    About ItemPipeline：
        spider在爬取网页的时候要分析网页的内容，并且从网页中提取有用的内容，这些内容就可以存放在item中，
        通过return item 或者 yield item 就可以把整个item的内容传递到pipeline，
        这个时候就可以在pipeline中写代码，把item的内容进行处理，比如删除重复的内容，或者把item存放到数据库中
    Spider Nodes：
        1、Intenet上的网页很多都是使用ajax等异步加载技术组成的，当爬取的网页中存在异步加载的情况是，
        使用scrapy爬取网页得到的相应内容中不一定存在你想要提取的目标。此时就需要使用浏览器的抓包工具进行抓包，
        先找到目标源数据包的位置、查看包的响应内容、查看包的请求参数和请求头信息。
        通过分析目标源包的请求参数等信息，使用伪装请求头和请求参数发送请求，进而得到目标数据
