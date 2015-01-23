#!/usr/bin/python

## @dataset_iterator.py
#  This file iterates a given dataset, and returns a list of dict records, of earthquakes
#      within the supplied parameters (i.e. radius, timeframe).
import json, time
from jsonschema import validate
from package.jsonschema_definitions import jsonschema_data

## Class: Data_Iterator
class Data_Iterator:

  ## constructor:
  def __init__(self, dataset, longitude, latitude, radius, daysBack):
    self.target   = []
    self.dataset  = dataset
    self.origin_longitude = longitude
    self.origin_latitude  = latitude
    self.radius   = radius
    self.daysBack = daysBack

    self.list_error = []

  ## iterator: iterate a given dataset, and store earthquakes within the specified radius,
  #            and timeframe.
  def iterator(self):
    for val in self.dataset['features']:
      # elements from supplied dataset
      id          = val['id']
      coordinates = val['geometry']['coordinates']
      magnitude   = val['properties']['mag']
      time        = val['properties']['time']
      location    = val['properties']['place']

      # create custom dataset instance, and validate
      data_instance = {'id': id, 'coordinates': coordinates, 'magnitude': magnitude, 'time': time, 'location': location}
      data_check  = self.validate_dataset(data_instance)

      # append dataset instance to target list, if within radius, and timeframe
      if self.validate_date(time) and data_check:
        self.target.append( {'id': id, 'coordinates': coordinates, 'magnitude': magnitude, 'time': time, 'location': location} )

  ## validate_dataset: validate subset(s) of given the dataset. The above 'iterator' method,
  #                    implements this method.
  def validate_dataset(self, data_instance):
    try:
      validate(data_instance, jsonschema_data())
      return True
    except Exception, error:
      self.list_error.append( {'class': 'Data_Iterator', 'method': 'validator', 'msg': error} )
      return False

  ## validate_date: validate if earthquake is within specified number of days.
  #
  #  @current_time, the current time in milliseconds.
  #  @allowed_difference, number of days in milliseconds.
  def validate_date(self, earthquake_time):
    current_time       = int(round(time.time() * 1000))
    allowed_difference = self.daysBack * 86400000

    if ( current_time - earthquake_time < allowed_difference ): return True
    else: return False

  ## get_targets: return a list of earthquakes within the supplied parameters.
  def get_targets(self):
    if len(self.target) > 0: return self.target
    else: return self.list_error

  ## get_largest_target: return largest single earthquake within the supplied parameters.
  def get_largest_target(self):
    if len(self.target) > 0:
      largest_magnitude = max( self.target, key=lambda x:x['magnitude'] )
      return largest_magnitude
    else: return self.list_error
