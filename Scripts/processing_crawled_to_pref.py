# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 21:05:10 2015

@author: Niklas Bendixen
"""

import os                                       # https://docs.python.org/2/library/os.html
import fnmatch                                  # https://docs.python.org/2/library/fnmatch.html
import re                                       # https://docs.python.org/2/library/re.html
import treetaggerwrapper as ttw                 # https://treetaggerwrapper.readthedocs.org/en/latest/
import rdflib                                   # https://rdflib.readthedocs.org/en/stable/
import rdflib.plugins.sparql as sparql          # https://rdflib.readthedocs.org/en/stable/apidocs/rdflib.plugins.sparql.html#module-rdflib.plugins.sparql
from rdflib import Graph                        # https://rdflib.readthedocs.org/en/stable/apidocs/rdflib.html#module-rdflib.graph
from rdflib.namespace import Namespace, SKOS    # https://rdflib.readthedocs.org/en/stable/apidocs/rdflib.html#module-rdflib.namespace


# 1. Removing CSS from the crawled Files
for dirpath, dirs, files in os.walk('originalfiles'):
    for filename in fnmatch.filter(files, '*_crawled.xml_clean.xml'):
        with open('originalfiles/'+filename, 'r') as originalfile, open('inbetween/'+filename[:-21]+'ohne_css_test.xml', 'w') as testfile, open('inbetween/'+filename[:-21]+'ohne_css_stw.xml', 'w') as stwfile:
            #print filename[:-21]
            for line in originalfile:
                if line.strip():
                    line = re.sub(r'[\w]*[:|.|#][\w]*[ ]?{[\w\W]*}', '', line, re.M)
                    testfile.write(line)
                    stwfile.write(line)


# 2. Removing XML Structure from crawled Files
replacements = {
                '<?xml version="1.0" encoding="utf-8"?>':'',
                '<root>':'',
                '<item>':'',
                '<fragment>':'',
                '</fragment>':'',
                '</item>':'',
                '</root>':''
                }

for dirpath, dirs, files in os.walk('inbetween'):
    for filename in fnmatch.filter(files, '*_ohne_css_stw.xml'):
        with open('inbetween/'+filename, 'r') as originalfile, open('inbetween/'+filename[:-7]+'xml_stw.xml', 'w') as stwfile:
                for line in originalfile:
                    for src, target in replacements.iteritems():
                        line = line.replace(src, target)
                    stwfile.write(line)
                    #print line


# 3. Removing German Stopwords from the Files
stopwords = []
# Download Link to the German Stopword List that is used here: http://members.unine.ch/jacques.savoy/clef/germanST.txt
with open('stopwords_german.txt', 'r') as stopwords_file:
    for line in stopwords_file:
        stopwords.append(line.strip())

for dirpath, dirs, files in os.walk('inbetween'):
    for filename in fnmatch.filter(files, '*_ohne_css_test.xml'):
        with open('inbetween/'+filename, 'r') as originalfile, open('inbetween/'+filename[:-8]+'stop_test.xml', 'w') as testfile:
                for line in originalfile:
                    line = line.split()
                    for n in line:
                        if n in stopwords:
                            pass
                        else:
                            testfile.write(n + ' ')
                            #print n

for dirpath, dirs, files in os.walk('inbetween'):
    for filename in fnmatch.filter(files, '*_ohne_css_xml_stw.xml'):
        with open('inbetween/'+filename, 'r') as originalfile, open('inbetween/'+filename[:-7]+'stop_stw.xml', 'w') as stwfile:
            for line in originalfile:
                line = line.split()
                for n in line:
                    if n in stopwords:
                        pass
                    else:
                        stwfile.write(n + ' ')
                        #print n


# 4. Lemmatizing and Tagging German Words
tagger = ttw.TreeTagger(TAGLANG='de')

for dirpath, dirs, files in os.walk('inbetween'):
    for filename in fnmatch.filter(files, '*_ohne_css_xml_stop_stw.xml'):
        tagger.tag_file_to('inbetween/'+filename, 'inbetween/'+filename[:-7]+'tagged_stw.xml')


replace = re.compile(r'^replaced-email|^replaced-dns|^<repemail|^<repdns')
for dirpath, dirs, files in os.walk('inbetween'):
    for filename in fnmatch.filter(files, '*_ohne_css_xml_stop_tagged_stw.xml'):
        with open('inbetween/'+filename, 'r') as originalfile, open('inbetween/'+filename[:-4]+'2.xml', 'w') as stwfile:
            #print filename
            for line in originalfile:
                line = line.strip()
                if replace.search(line) is not None:
                    #print line
                    pass
                else:
                    line = line.split('\t')
                    if len(line) != 3:
                        #print len(line)
                        pass
                    else:
                        #print line[0] + '\t' + line[1] + '\t' + line[2]
                        stwfile.write(line[0] + '\t' + line[1] + '\t' + line[2] + '\n')


# 5. Processing STW Files to get skos:prefLabel
GBV = Namespace('http://purl.org/ontology/gbv/#')
STW = Namespace('http://zbw.eu/stw/')
ZBWTEXT = Namespace('http://zbw.eu/namespaces/zbw-extensions/')

g = Graph()
# Download Link to the RDF File from the STW Thesaurus for Economics that is used here: http://zbw.eu/stw/versions/latest/download/about.en.html
g.parse('stw.rdf', format='xml')

q_pref = sparql.prepareQuery('SELECT ?o WHERE { ?s ?pref ?o . }')
q_alt= sparql.prepareQuery('SELECT ?x WHERE { ?s ?alt ?o . ?s ?pref ?x . FILTER (lang(?x) = "de")}')

pref = SKOS.prefLabel
alt = SKOS.altLabel

for dirpath, dirs, files in os.walk('inbetween'):
    for filename in fnmatch.filter(files, '*_ohne_css_xml_stop_tagged_stw2.xml'):
        with open('inbetween/'+filename, 'r') as openfile, open('inbetween/'+filename[:-33]+'nur_pref_stw.xml', 'w') as preffile, open('inbetween/'+filename[:-33]+'tag_und_pref_stw.xml', 'w') as tagfile:
            #print filename
            for n in openfile:
                #print n
                #print filename + ' TEST ' + '\n'
                n = n.strip().split('\t')
                #print len(n)
                #print n[1]
                #print n
                #print filename + ' ' + n[2]
                if re.match(r'[NN|NE]', n[1]):
                    #print n[0] + ' ' + n[1]
                    #testword = n[0]
                    #print testword
                    #o = rdflib.Literal(testword, lang='de')
                    o = rdflib.Literal(n[0], lang='de')

                    q_pref_res = g.query(q_pref, initBindings={'pref' : pref, 'o' : o})
                    #print 'Length q_pref_res: '
                    #print len(q_pref_res)

                    if len(q_pref_res) == 1:
                       for row in g.query(q_pref, initBindings={'pref' : pref, 'o' : o}):
                           #pass
                            #print n[0]
                            #print n[0] + '\t' + n[1] + '\t' + str(row)
                            preffile.write(n[0] + '\n')
                            tagfile.write(n[0] + '\t' + n[1] + '\t' + str(row) + '\n')
                    elif len(q_pref_res) == 0:
                        q_alt_res = g.query(q_alt, initBindings={'alt' : alt, 'o' : o, 'pref' : pref})
                        if len(q_alt_res) == 1:
                            #print 'Length q_alt_res: '
                            #print len(q_alt_res)
                            for row in g.query(q_alt, initBindings={'alt' : alt, 'o' : o, 'pref' : pref}):
                                #pass
                                #print n[0] + '\t' + n[1] + '\t' + str(row)
                                #print row
                                preffile.write(str(row) + '\n')
                                tagfile.write(n[0] + '\t' + n[1] + '\t' + str(row) + '\n')


# 6. Remove Strings from STW Files to get only skos:prefLabel in the Files
replacements_stw = {
                    '(rdflib.term.Literal(u\'': '',
                    '\', lang=u\'de\'),)': '',
                    '\', lang=\'de\'),)': ''
                    }
replacements_stw = dict((re.escape(k), v) for k, v in replacements_stw.iteritems())
pattern = re.compile('|'.join(replacements_stw.keys()))

for dirpath, dirs, files in os.walk('inbetween'):
    for filename in fnmatch.filter(files, '*_nur_pref_stw.xml'):
        with open('inbetween/'+filename, 'r') as openfile, open('outputfiles/1/'+filename[:-7]+'clean_stw.xml', 'w') as newfile:
            #print filename
            for line in openfile:
                line = pattern.sub(lambda m: replacements_stw[re.escape(m.group(0))], line)
                #print line.strip()
                newfile.write(line)


for dirpath, dirs, files in os.walk('inbetween'):
    for filename in fnmatch.filter(files, '*_tag_und_pref_stw.xml'):
        with open('inbetween/'+filename, 'r') as openfile, open('inbetween/'+filename[:-7]+'clean_stw.xml', 'w') as newfile:
            #print filename
            for line in openfile:
                line = pattern.sub(lambda m: replacements_stw[re.escape(m.group(0))], line)
                newfile.write(line)


# 7. Replace skos:altLabel with skos:prefLabel in the Files
for dirpath, dirs, files in os.walk('inbetween'):
    for filename in fnmatch.filter(files, '*_ohne_css_stop_test.xml'):
        with open('inbetween/'+filename, 'r') as openfile, open('outputfiles/2/'+filename[:-22]+'pref_ersetzt.xml', 'w') as newfile:
            #print filename
            #print 'Neue Schleife! '
            for dirpath2, dirs2, files2 in os.walk('inbetween'):
                for filename2 in fnmatch.filter(files2, filename[:-22]+'tag_und_pref_clean_stw.xml'):
                    prefLabel = {}
                    with open('inbetween/'+filename2, 'r') as prefLabelFile:
                        #print filename2
                        #print prefLabel
                        for line in prefLabelFile:
                            line = line.split()
                            prefLabel[line[0]] = line[2]
                    #print prefLabel
            for line in openfile:
                line = line.split()
                for i in line:
                    for key, value in prefLabel.items():
                        if i in key:
                            #print i
                            i = value
                            #print i + ' '
                    newfile.write(i + ' ')