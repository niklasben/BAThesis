# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 15:50:53 2015

@author: Niklas Bendixen
"""

from scrapy.linkextractors import LinkExtractor     # http://doc.scrapy.org/en/1.0/topics/link-extractors.html
from scrapy.loader import ItemLoader                # http://doc.scrapy.org/en/1.0/topics/loaders.html
from scrapy.selector import Selector                # http://doc.scrapy.org/en/latest/topics/selectors.html
from scrapy.spiders import CrawlSpider, Rule        # http://doc.scrapy.org/en/latest/topics/spiders.html#generic-spiders

from Scrapy_One.items import Items_Main


class MySpider(CrawlSpider):

    name = 'spiderName'
    allowed_domains = ['ziegenhof-schleckweda.de']
    start_urls = ['http://www.ziegenhof-schleckweda.de/cont_Home/home.html']
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
            loader.add_xpath('fragment', '//*[not(self::script)]/text()')
            items_main.append(loader.load_item())
            return items_main