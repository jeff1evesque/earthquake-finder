#!/usr/bin/python

## @json_scraper.py
#  This file scrapes the content of an external webpage, and returns the
#      parsed response to javascript (retriever_dataset.js) via AJAX.
import urllib2

## scrape: scrape the content of provided url.
def scrape(url):
  # open given url, store the corresponding json response
  response = urllib2.urlopen(url)
  data     = response.read()
  response.close()

  # return content
  return data
