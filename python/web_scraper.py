#!/usr/bin/python

## @web_scraper.py
#  This file scrapes the content of an external webpage.
from lxml import html
import requests, sys

if len( sys.argv ) > 0:
  # retrieve webpage, store the corresponding content
  webpage = requests.get(sys.argv[1])
  content = html.fromstring(webpage.text)
