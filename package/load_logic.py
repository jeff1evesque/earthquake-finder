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
from package.validator_functions import validate_longitude, validate_latitude, validate_radius, validate_daysBack, validate_dataset_url
import json

## earthquake_finder: determine largest magnitude earthquake using given parameters.
#
#  @dict_request, must be a dictionary with the following structure:
#
#      { 'longitude': aa.aa, 'latitude': bb.bb, 'radius': cc.cc,
#        'daysBack': dd, 'dataset': ee }
#
#          aa.aa: float value between [-180, 180]
#          bb.bb: float value between [-90, 90]
#          cc.cc: positive float value
#          dd   : positive integer
#          ee   : valid URL.
def earthquake_finder(dict_request):
  # validate parameters
  flag_request = validate_request( dict_request )

  if flag_request['status']:
    # get dataset from external webpage
    dataset = scrape(dict_request['dataset'])

    # parse dataset for target(s) within specified parameters
    target = Data_Iterator( dataset, dict_request )
    target.iterator()
    target_return = target.get_largest_target()

    # return result(s) to browser
    return json.dumps(target_return)
  else: return json.dumps({ 'data': None, 'error': flag_request['error'] })

if __name == '__main__':
  longitude = raw_input('Enter longitude [-180, 180]: ')
  latitude  = raw_input('Enter latitude [-90, 90]: ')
  radius    = raw_input('Enter radius: ')
  daysBack  = raw_input('Enter days back: ')
  dataset   = raw_input('Enter dataset url: ')

  dict_request = { 'longitude': longitude, 'latitude': latitude, 'radius': radius, 'daysBack': daysBack, 'dataset': dataset }

  # return largest magnitude earthquake
  earthquake = earthquake_finder( dict_request )
  print earthquake
