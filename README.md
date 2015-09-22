# BAThesis
Files to graduate as a Bachelor of Arts in Information Management from the University of Applied Sciences and Arts in Hanover.

## Crawler
I used [Scrapy](http://scrapy.org/) to crawl the Websites for this Project.

## Scripts
This Folder contains the used German Stopword List as a txt-File, the STW Thesaurus for Economics as rdf-File and two Python Scripts.

## Files_Crawled
Storage Folder for the crawled Website-Files with some re-structuring to make them easier readable by human beings.

## Files_Machine_Learning
Folder where the crawled Websites are stored after the processing via [processing_crawled_to_pref.py](https://github.com/niklasben/BAThesis/blob/master/Scripts/processing_crawled_to_pref.py). One Folder for the whole Text, excluding German Stopwords, and replaced *skos:altLabel* with *skos:prefLabel* and one Folder only for the stored *skos:prefLabel*.
