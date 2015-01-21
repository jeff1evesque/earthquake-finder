#!/usr/bin/python

## @json_scraper.py
#  This file scrapes the content of an external webpage, and returns the
#      parsed json response to javascript (retriever_dataset.js) via AJAX.
import sys, urllib2, json

## scraper: scrape the content of provided url.
def scraper():
  if len( sys.argv ) > 0:
    # open given url, store the corresponding json response
    response = urllib2.urlopen(sys.argv[1])
    data     = json.load(response)
    response.close()

    # return content
    print data
