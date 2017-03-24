# !/usr/bin/python
# -*- coding: utf-8 -*-


BOT_NAME = 'wwwSpider'

SPIDER_MODULES = ['wwwSpider.spiders']
NEWSPIDER_MODULE = 'wwwSpider.spiders'

ROBOTSTXT_OBEY = False

COOKIES_ENABLED = False

# 当要使用pipeline时，需要配置pipeline
# 保存项目中启用的pipeline及其顺序的字典。值(value)习惯设定在0-1000范围内
ITEM_PIPELINES = {
    'wwwSpider.pipelines.WwwspiderPipeline': 300,
}

# 下载器在下载同一个网站下一个页面前需要等待的时间。该选项可以用来限制爬取速度， 减轻服务器压力。同时也支持小数:
DOWNLOAD_DELAY = 0.01

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# 下载器超时时间(单位: 秒)。
# DOWNLOAD_TIMEOUT = 180


################## splash渲染器配置  #########################

# splash渲染器服务器地址
SPLASH_URL = ''

# 将splash middleware添加到DOWNLOADER_MIDDLEWARE中：
DOWNLOADER_MIDDLEWARES = {
'scrapy_splash.SplashCookiesMiddleware': 723,
'scrapy_splash.SplashMiddleware': 725,
'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

# Enable SplashDeduplicateArgsMiddleware:
SPIDER_MIDDLEWARES = {
'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

# Set a custom DUPEFILTER_CLASS:
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

# a custom cache storage backend:
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

################## splash渲染器配置  #########################


# 爬取的默认User-Agent，除非被覆盖
USER_AGENT = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
]

# 如果启用，当从相同的网站获取数据时，Scrapy将会等待一个随机的值 (0.5到1.5之间的一个随机值 * DOWNLOAD_DELAY)。
# 该随机值降低了crawler被检测到(接着被block)的机会。某些网站会分析请求， 查找请求之间时间的相似性。
# 若 DOWNLOAD_DELAY 为0(默认值)，该选项将不起作用。
# RANDOMIZE_DOWNLOAD_DELAY = True

# Item Processor(即 Item Pipeline) 同时处理(每个response的)item的最大值。
#CONCURRENT_ITEMS = 100

# 对单个网站进行并发请求的最大值。
# CONCURRENT_REQUESTS_PER_DOMAIN = 8

# The download delay setting will honor only one of:
# Scrapy downloader 并发请求(concurrent requests)的最大值。
#CONCURRENT_REQUESTS_PER_DOMAIN = 16


# 对单个IP进行并发请求的最大值。如果非0，则忽略 CONCURRENT_REQUESTS_PER_DOMAIN 设定，使用该设定。
#  也就是说，并发限制将针对IP，而不是网站。
# 该设定也影响 DOWNLOAD_DELAY: 如果 CONCURRENT_REQUESTS_PER_IP 非0，下载延迟应用在IP而不是网站上。
#CONCURRENT_REQUESTS_PER_IP = 16

# the Scrapy shell 中实例化item使用的默认类。
# DEFAULT_ITEM_CLASS = 'scrapy.item.Item'

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# Scrapy HTTP Request使用的默认header。由 DefaultHeadersMiddleware 产生。
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# 爬取网站最大允许的深度(depth)值。如果为0，则没有限制。
# DEPTH_LIMIT = 0

# 整数值。用于根据深度调整request优先级。如果为0，则不根据深度进行优先级调整。
# DEPTH_PRIORITY = 0

# 是否收集最大深度数据
# DEPTH_STATS = True

# 是否收集详细的深度数据。如果启用，每个深度的请求数将会被收集在数据中。
# DEPTH_STATS_VERBOSE = False

# 是否启用DNS内存缓存(DNS in-memory cache)。
# DNSCACHE_ENABLED = True

# 用于crawl的downloader.
# DOWNLOADER = 'scrapy.core.downloader.Downloader'

# 保存项目中启用的下载中间件及其顺序的字典
# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'wwwSpider.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# 是否收集下载器数据
# DOWNLOADER_STATS = True

# 保存项目中启用的下载处理器(request downloader handler)的字典
# DOWNLOAD_HANDLERS = {}

# 保存项目中默认启用的下载处理器(request downloader handler)的字典。 永远不要在项目中修改该设定，而是修改 DOWNLOADER_HANDLERS
# DOWNLOAD_HANDLERS_BASE =
# {
#     'file': 'scrapy.core.downloader.handlers.file.FileDownloadHandler',
#     'http': 'scrapy.core.downloader.handlers.http.HttpDownloadHandler',
#     'https': 'scrapy.core.downloader.handlers.http.HttpDownloadHandler',
#     's3': 'scrapy.core.downloader.handlers.s3.S3DownloadHandler',
# }
# 如果需要关闭上面的下载处理器，您必须在项目中的 DOWNLOAD_HANDLERS 设定中设置该处理器，并为其赋值为 None 。 例如，关闭文件下载处理器:
# DOWNLOAD_HANDLERS = {
#     'file': None,
# }

# 用于检测过滤重复请求的类。
# 默认的 (RFPDupeFilter) 过滤器基于 scrapy.utils.request.request_fingerprint 函数生成的请求fingerprint(指纹)。
# 如果您需要修改检测的方式，您可以继承 RFPDupeFilter 并覆盖其 request_fingerprint 方法。
# 该方法接收 Request 对象并返回其fingerprint(一个字符串)。
# DUPEFILTER_CLASS = 'scrapy.dupefilter.RFPDupeFilter'

# 保存项目中启用的插件及其顺序的字典。
# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# 可用的插件列表。需要注意，有些插件需要通过设定来启用。默认情况下， 该设定包含所有稳定(stable)的内置插件。
# EXTENSIONS_BASE =
# {
#     'scrapy.contrib.corestats.CoreStats': 0,
#     'scrapy.webservice.WebService': 0,
#     'scrapy.telnet.TelnetConsole': 0,
#     'scrapy.contrib.memusage.MemoryUsage': 0,
#     'scrapy.contrib.memdebug.MemoryDebugger': 0,
#     'scrapy.contrib.closespider.CloseSpider': 0,
#     'scrapy.contrib.feedexport.FeedExporter': 0,
#     'scrapy.contrib.logstats.LogStats': 0,
#     'scrapy.contrib.spiderstate.SpiderState': 0,
#     'scrapy.contrib.throttle.AutoThrottle': 0,
# }


# 是否启用logging。
# LOG_ENABLED = True

# logging使用的编码。
# LOG_ENCODING = 'utf-8'

# logging输出的文件名。如果为None，则使用标准错误输出(standard error)。
# LOG_FILE = None

# log的最低级别。可选的级别有: CRITICAL、 ERROR、WARNING、INFO、DEBUG。更多内容请查看 Logging 。
# LOG_LEVEL = 'DEBUG'

# 如果为 True ，进程所有的标准输出(及错误)将会被重定向到log中。例如， 执行 print 'hello' ，其将会在Scrapy log中显示。
# LOG_STDOUT = False

# 是否启用内存调试(memory debugging)。
# MEMDEBUG_ENABLED = False

# 如果该设置不为空，当启用内存调试时将会发送一份内存报告到指定的地址；否则该报告将写到log中。
# MEMDEBUG_NOTIFY = []
# 样例: MEMDEBUG_NOTIFY = ['user@example.com']

# 是否启用内存使用插件。当Scrapy进程占用的内存超出限制时，该插件将会关闭Scrapy进程， 同时发送email进行通知。
# MEMUSAGE_ENABLED = False
# Scope: scrapy.contrib.memusage

# 在关闭Scrapy之前所允许的最大内存数(单位: MB)(如果 MEMUSAGE_ENABLED为True)。 如果为0，将不做限制。
# MEMUSAGE_LIMIT_MB = 0
# Scope: scrapy.contrib.memusage

# 达到内存限制时通知的email列表。
# MEMUSAGE_NOTIFY_MAIL = False
# Scope: scrapy.contrib.memusage
# Example:MEMUSAGE_NOTIFY_MAIL = ['user@example.com']

# telnet终端使用的端口范围。如果设置为 None 或 0 ， 则使用动态分配的端口
# TELNETCONSOLE_PORT = [6023, 6073]


# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# 保存项目中启用的下载中间件及其顺序的字典
#SPIDER_MIDDLEWARES = {
#    'wwwSpider.middlewares.MyCustomSpiderMiddleware': 543,
#}


# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
