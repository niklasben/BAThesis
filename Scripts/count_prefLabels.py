# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 14:56:05 2015

@author: Niklas Bendixen
"""

import os       # https://docs.python.org/2/library/os.html
import fnmatch  # https://docs.python.org/2/library/fnmatch.html

with open('../Scripts/prefLabels_counted.tex', 'w') as newfile:
    for dirpath, dirs, files in os.walk('../Files_Machine_Learning/prefLabel'):
        newfile.write('% Beginn Anhang Liste prefLabel\n')
        newfile.write('%\n')
        newfile.write('\\section{Anzahl skos:prefLabel bei gecrawlten Websites}\\label{sec:listepreflabel}\n')
        newfile.write('\\begin{longtable}{|m{0.5cm}||m{8cm}|m{5cm}|}\n')
        newfile.write('\t\\caption{Liste skos:prefLabel bei gecrawlten Websites}\\label{tbl:preflabel}\\\\%Verweis im Text mittels \\ref{tbl:preflabel}\n')
        newfile.write('\t\\hline\n')
        newfile.write('\t\\textbf{Nr.} & \\textbf{Website} & \\textbf{Anzahl skos:prefLabel} \\\\\n')
        newfile.write('\t\hline \\hline\n')
        count_file = 0
        count_nr = 0
        for filename in fnmatch.filter(files, '*.xml'):
            count_nr = count_nr +1
        count_nr
        for filename in fnmatch.filter(files, '*.xml'):
            with open('../Files_Machine_Learning/prefLabel/'+filename, 'r') as originalfile:
                count_file = count_file+1
                count_label = 0
                for line in originalfile:
                    count_label = count_label +1
                #print str(count_file) + ' ' + str(filename[:-14]) + ': ' + str(count_label)
                newfile.write('\t' + str(count_file) + ' & ' + str(filename[:-14]) + ' & ' + str(count_label) + '\\\\\n')
                if count_file < count_nr:
                    newfile.write('\t\\hline\n')
                else:
                    newfile.write('\t\\lasthline\n')
        newfile.write('\\end{longtable}\n')
        newfile.write('%\n')
        newfile.write('% Ende Anhang Liste prefLabel')