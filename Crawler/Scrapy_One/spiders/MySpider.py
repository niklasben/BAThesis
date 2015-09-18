# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 15:50:53 2015

@author: Niklas Bendixen
"""

#import urlparse
#import csv
#import re
#import scrapy


#from scrapy import signals
#from scrapy.crawler import CrawlerRunner
#from scrapy.http import Request, HtmlResponse
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
#from scrapy.loader.processors import Compose, MapCompose, Join, TakeFirst
from scrapy.selector import Selector
#from scrapy.settings import Settings
from scrapy.spiders import CrawlSpider, Rule #, Spider
#from scrapy.utils.log import configure_logging
#from scrapy.utils.markup import remove_tags, remove_tags_with_content
#from scrapy.utils.response import get_base_url
#from scrapy.utils.url import urljoin_rfc
#from scrapy.xlib.pydispatch import dispatcher

#from twisted.internet import reactor
#from w3lib.html import replace_escape_chars, remove_tags

from Scrapy_One.items import Items_Main


class MySpider(CrawlSpider):

    name = 'spiderName'
#    allowed_domains = ['ziegenhof-schleckweda.de']
#    start_urls = ['http://www.ziegenhof-schleckweda.de/cont_Home/home.html']
    allowed_domains = ['ingress.com']
    start_urls = ['http://www.ingress.com/']
    rules = (Rule(LinkExtractor(allow = ('', ),
                                deny = ('/(language/en/home/|/corporate/en_de/|de-at/|de-ch/|en/|en-ca/|en-CA/|en-GB/|en-hr/|en-in/|en-sg/|en-ph/|en-za/|en-AU/|en-gb/|en-UK/|en-us/|en-US/|en-europe/|en-americalatina/|en-asiapacific/|english/|englisch/|bg-bg/|be/|belgisch/|cz/|cs-cz/|česky/|cn/|da-dk/|es/|es-es/|es-ar/|es-cl/|es-mx/|es-americalatina/|fi/|fi-fi/|fr-fr/|fr/|fr-CA/|franzoesisch/|français/|ht-hr/|hr-hr/|hu/|hu-hu/|it/|it-it/|italienisch/|italiano/|jp/|ko-kr/|lt/|lt-lt/|lv/|lv-lv/|nl/|nl-nl/|nl-NL/|nl-be/|niederlaendisch/|nederlands/|no/|nb-no/|norwegisch/|pl/|pl-pl/|polski/|pt/|pt-br/|pt-americalatina/|ro/|se/|sv-se/|schwedisch/|svenska/|sk/|tr/|tr-tr/|ru/|ru-ru/|pусский/|sk/|sk-sk/|sl-si/|zh/|zh-cn/|zhcn-asiapacific/|zh-tw/|zhtw-asiapacific/|cn/|gr/)|(\w|\W)*([Ii]mpressum|[Aa]bout|AGB|[Ii]mprint|[Pp]rivacy|[Tt]erms|[Cc]opyright|[Hh]elp|[Hh]ilfe|[Ii]mage[s]?|[Bb]ild[er]?|[Dd]atenschutz|[KkCc]onta[kc]t|[Rr]echtliche(\w|\W)*[Hh]inweis|[Hh]aftungsausschlu)'),
                                unique = True),
                                callback = 'parse_stuff',
                                follow = True),
            )


    def parse_stuff(self, response):
        hxs = Selector(response)
        sites = hxs.xpath('//body')
        items_main = []

        for site in sites:
            loader = ItemLoader(item = Items_Main(), response = response)
#            loader.default_input_processor = MapCompose(lambda v: v.strip(), replace_escape_chars)
#            loader.add_xpath('a_title', '//head/title/text()')
#            loader.add_xpath('defined', '//*[@id="quote-text"]/text()')
            loader.add_xpath('fragment', '//*[not(self::script)]/text()')
#            loader.add_xpath('fragment', './/h2/text()')
#            loader.add_xpath('fragment', './/h3/text()')
#            loader.add_xpath('fragment', '//div//text()')
#            loader.add_xpath('links', '//*/a/@href')
            items_main.append(loader.load_item())
            return items_main

'''
# Class for automated crawling of n domains from a txt-file.
# Will be exported in one xml-file.

class AutoSpider(CrawlSpider):

    name = 'autoSpider'

    read_urls = open('../../urls.txt', 'r')
    allowed_domains = []
    start_urls = []
    for url in read_urls.readlines():
        url = url.strip()
        allowed_domains = allowed_domains + [url[4:]]
        start_urls = start_urls + ['http://' + url]
        rules = (Rule(LinkExtractor(allow = ('', ),
                                deny = ('/(\w|\W)*([Ii]mpressum|[Aa]bout|[Pp]rivacy|[Tt]erms|[Cc]opyright|[Hh]elp|[Hh]ilfe|[Dd]atenschutz|[Rr]echtliche(\w|\W)*[Hh]inweis|[Hh]aftungsausschlu)'),
                                unique = True),
                                callback = 'parse_auto',
                                follow = True),
                )


    def parse_auto(self, response):
        hxs = Selector(response)
        sites = hxs.xpath('//html')
        items_main = []

        for site in sites:
            loader = ItemLoader(item = Items_Main(), response = response)
#            loader.default_input_processor = MapCompose(lambda v: v.strip(), replace_escape_chars)
            loader.add_xpath('a_title', '//head/title/text()')
            loader.add_xpath('defined', '//*[@id="quote-text"]/text()')
            loader.add_xpath('fragment', '//*[not(self::script)]/text()')
            loader.add_xpath('links', '//*/a/@href')
            items_main.append(loader.load_item())
            return items_main
'''
'''
# Rules without the deny() argument

    rules = (Rule(LinkExtractor(allow = ('', ),
                                unique = True),
                                callback = 'parse_stuff',
                                follow = True),
            )
'''