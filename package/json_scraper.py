#!/usr/bin/python

## @json_scraper.py
#  This file makes a request to an external webpage, and returns the json
#      response content.
import requests

## scrape: scrape the content of provided url.
def scrape(url):
  # open given url, store the corresponding json response
  r = requests.get(url)
  data = r.json()

  # return content
  return data
