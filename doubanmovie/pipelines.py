# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


#class DoubanmoviePipeline(object):
#    def process_item(self, item, spider):
#        return item


from scrapy import signals
import json
import codecs

# 如下设置，将爬取到的内容保存到movie.json文件中，编码方式为utf-8，能直接看。
class DoubanmoviePipeline(object):
    def __init__(self):
        self.file = codecs.open('movie.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()