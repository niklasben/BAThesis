# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 15:50:53 2015

@author: Niklas Bendixen
"""

# Scrapy settings for Scrapy_One project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

#import os
#import sys
#
#from importlib import import_module
#from os.path import join, abspath, dirname


SPIDER_MODULES = ['Scrapy_One.spiders']

ITEM_PIPELINES = {
    'Scrapy_One.pipelines.XmlExportPipeline': 800,
}

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'de',
}

DOWNLOAD_HANDLERS = {
    's3': None,
}

COOKIES_ENABLED = False
COOKIES_DEBUG = True

CLOSESPIDER_PAGECOUNT = 400

DOWNLOAD_DELAY = 2

DEPTH_LIMIT = 3
#DEPTH_LIMIT = 1

IGNORED_EXTENSIONS = [
    # images
    'mng', 'pct', 'bmp', 'gif', 'jpg', 'jpeg', 'png', 'pst', 'psp', 'tif',
    'tiff', 'ai', 'drw', 'dxf', 'eps', 'ps', 'svg', 'tga', 'jbig',

    # audio
    'mp2', 'mp3', 'wma', 'ogg', 'wav', 'ra', 'aac', 'mid', 'au', 'aiff', 'm4b',
    'm4p', 'm4r', 'rm',

    # video
    '3gp', 'asf', 'asx', 'avi', 'mov', 'mp4', 'mpg', 'mpeg', 'qt', 'rm', 'ram',
    'swf', 'wmv', 'm4a', 'm4v', 'mp4v',

    # office suites
    'xls', 'xlsx', 'ppt', 'pptx', 'doc', 'docx', 'odt', 'ods', 'odg', 'odp',

    # other
    'css', 'pdf', 'exe', 'bin', 'rss', 'zip', 'rar', 'js', 'gz', '7z', 'smil',
]