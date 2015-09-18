# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:38:24 2015

@author: Niklas
"""

import os
import fnmatch

replacements = {
                '<root>':'<root>',
                '<item>':'\n<item>',
                '<fragment>':'\n<fragment>\n',
                '</fragment>':'\n</fragment>',
                '</item>':'\n</item>',
                '</root>':'\n</root>'
                }

for dirpath, dirs, files in os.walk('output_cleaned'):
    for filename in fnmatch.filter(files, '*.xml'):
        with open('output_cleaned/'+filename, 'r') as originalfile, open('output_cleaned/Done/'+filename+'_clean.xml', 'w') as newfile:
            for line in originalfile:
                for src, target in replacements.iteritems():
                    line = line.replace(src, target)
                newfile.write(line)
#                print line
            newfile.close()
            originalfile.close()