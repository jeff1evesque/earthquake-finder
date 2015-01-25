#!/usr/bin/python

## @load_logic.py
#  This file contains the necessary logic needed to determine the largest magnitude
#      earthquake from the given dataset, relative to the supplied GPS coordinates,
#      with respect to the acceptable radius, and number of days back from today
#      (when webform, or command is submitted).
#
#  Specifically, this file can be run via the command line, or via the supplied
#      web-interface (app.py). Form more information, refer to the README.md.
from package.json_scraper import scrape
from package.dataset_iterator import Data_Iterator
from package.validator_request import validate_request
import json
