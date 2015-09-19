# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 15:50:53 2015

@author: Niklas Bendixen
"""

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field 				# http://doc.scrapy.org/en/1.0/topics/items.html
from scrapy.loader.processors import MapCompose, Join 	# http://doc.scrapy.org/en/1.0/topics/loaders.html#declaring-input-and-output-processors
from w3lib.html import replace_escape_chars, remove_tags 	# https://w3lib.readthedocs.org/en/latest/w3lib.html#module-w3lib.html


class Items_Main(Item):
#   Define the fields for your item here like: name = Field()
    fragment = Field(
        input_processor = MapCompose(lambda v: v.strip(), remove_tags, replace_escape_chars),
        output_processor = Join(),
    )
#    links = Field(
#        input_processor = MapCompose(lambda v: v.strip(), remove_tags, replace_escape_chars),
#        output_processor = Join(),
#    )
#    links = Field()
#    pass