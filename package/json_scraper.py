#!/usr/bin/python

## @json_scraper.py
#  This file scrapes the content of an external webpage, and returns the
#      parsed json response to javascript (retriever_dataset.js) via AJAX.
import sys, urllib2

## scrape: scrape the content of provided url.
def scrape(url):
  # open given url, store the corresponding json response
  response = urllib2.urlopen(url)
  data     = json.loads(response)
  response.close()

  # return content
  return data
