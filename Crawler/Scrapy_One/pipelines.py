# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 15:50:53 2015

@author: Niklas Bendixen
"""

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

#import json
#import re

from scrapy import signals
from scrapy.exporters import XmlItemExporter


class XmlExportPipeline(object):
    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        xml_name = str(spider.allowed_domains)
        xml_name = xml_name[2:-2]
        file = open('../output/%s_crawled.xml' % xml_name, 'w+b')
#        file = open('../output/bauer_kirch_crawled.xml', 'w+b')
        self.files[spider] = file
        self.exporter = XmlItemExporter(file, root_element = 'root', item_element = 'item')
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item