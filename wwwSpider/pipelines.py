# !/usr/bin/python
# -*- coding: utf-8 -*-

# import pymongo
"""
这是一个将item存储到moongodb数据库的Demo
需要安装pymongo，这是python连接mongodb数据库的库
pip install pymongo
"""

"""
当爬虫代码中进行return item或者yield item是，
并且在settings.py中为WwwspiderPipeline配置ITEM_PIPELINES时，

return item或者yield item就可以把整个item的内容传递到pipeline，
这个时候就可以在pipeline中写代码，把item的内容进行处理，比如删除重复的内容，或者把item存放到数据库中

"""

class WwwspiderPipeline(object):
    """
    def __init__(self):
        # 连接数据库
        # host：数据库的IP
        # port：数据库的端口号
        self.client = pymongo.MongoClient(host='', port=12356)
        # 使用用户名和密码登录MongoDB
        # self.client.admin.authenticate('readwrite', 'wersdfxcv234')
        # 获得数据库的句柄
        # databaseName数据库名
        self.db = self.client['databaseName']

    def process_item(self, item, spider):
        dict_item = dict(item)
        coll = self.db['video']
        coll.insert_one(dict_item)
        return item


    def close_spider(self, spider):
        self.client.close()
    """

    def process_item(self, item, spider):
        print item
        return item
