#!/usr/bin/python

## @dataset_iterator.py
#  This file iterates a given dataset, and returns a list of dict records, of earthquakes
#      within the supplied parameters (i.e. radius, timeframe).
import json

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
      self.target.append(val)

  ## validator: validate subset(s) of given the dataset. The above 'iterator' method,
  #             implements this method.
  def validator(self):
    return 'STUB'

  ## get_targets: return a list of earthquakes within the supplied parameters.
  def get_targets(self):
    return self.target

  ## get_largest_target: return largest single earthquake within the supplied parameters.
  def get_largest_target(self):
    return self.target
