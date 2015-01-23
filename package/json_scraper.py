#!/usr/bin/python

## @json_scraper.py
#  This file scrapes the content of an external webpage, and returns the
#      parsed response to javascript (retriever_dataset.js) via AJAX.
import requests

## scrape: scrape the content of provided url.
def scrape(url):
  # open given url, store the corresponding json response
  r = requests.get(url)
  data = r.json()

  # return content
  return data
