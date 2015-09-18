# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 15:50:53 2015

@author: Niklas Bendixen
"""

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

#import scrapy

from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, Join, TakeFirst #, Compose
#from scrapy.utils.markup import remove_tags, remove_tags_with_content

from w3lib.html import replace_escape_chars, remove_tags
#from w3lib.html import replace_escape_chars, remove_tags_with_content, remove_tags


class Items_Main(Item):
#   Define the fields for your item here like: name = Field()
#    a_title = Field(
#        input_processor = MapCompose(lambda v: v.strip(), remove_tags, replace_escape_chars),
#        output_processor = TakeFirst(),
#    )
#    defined = Field(
#        input_processor = MapCompose(lambda v: v.strip(), remove_tags, replace_escape_chars),
#        output_processor = Join(),
#    )
    fragment = Field(
        input_processor = MapCompose(lambda v: v.strip(), remove_tags, replace_escape_chars),
        output_processor = Join(),
    )
#        fragment = Field(
#        input_processor = MapCompose(lambda v: v.strip(), remove_tags_with_content(v, which_ones('<script>',)), replace_escape_chars),
#        output_processor = Join(),
#    )
#    links = Field(
#        input_processor = MapCompose(lambda v: v.strip(), remove_tags, replace_escape_chars),
#        output_processor = Join(),
#    )
#    links = Field()
#    pass