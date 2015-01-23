#!/usr/bin/python

## @dataset_iterator.py
#  This file iterates a given dataset, and returns a list of dict records, of earthquakes
#      within the supplied parameters (i.e. radius, timeframe).
import json, time

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

  ## iterator: iterate a given dataset, and store earthquakes within the specified radius,
  #            and timeframe.
  def iterator(self):
    for val in self.dataset['features']:
      id          = val['id']
      coordinates = val['geometry']['coordinates']
      magnitude   = val['properties']['mag']
      time        = val['properties']['time']
      location    = val['properties']['place']

      self.target.append( {'id': id, 'coordinates': coordinates, 'magnitude': magnitude, 'time': time, 'location': location} )

  ## validator: validate subset(s) of given the dataset. The above 'iterator' method,
  #             implements this method.
  def validator(self):
    return 'STUB'

  ## validate_date: validate if earthquake is within specified number of days
  def validate_date(self, time):
    current_time = int(round(time.time() * 1000))

  ## get_targets: return a list of earthquakes within the supplied parameters.
  def get_targets(self):
    return self.target

  ## get_largest_target: return largest single earthquake within the supplied parameters.
  def get_largest_target(self):
    largest_magnitude = max( self.target, key=lambda x:x['magnitude'] )      
    return largest_magnitude
