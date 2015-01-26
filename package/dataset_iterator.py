#!/usr/bin/python

## @dataset_iterator.py
#  This file iterates a given dataset, and returns a list of dict records, of earthquakes
#      within the supplied parameters (i.e. radius, timeframe).
import json, time
from jsonschema import validate
from package.jsonschema_definitions import jsonschema_data
from package.haversine import get_distance

## Class: Data_Iterator
class Data_Iterator:

  ## constructor:
  #
  # @self.radius, the supplied radius (miles) is converted into meters
  #
  # Note: 'origin' pertains to parameters related to GPS coordinate supplied by the user,
  #       not the GPS coordinates related to the dataset.
  def __init__(self, dataset, origin):
    self.target   = []
    self.dataset  = dataset
    self.origin_longitude = float(origin['longitude'])
    self.origin_latitude  = float(origin['latitude'])
    self.radius   = float(origin['radius']) * 1609.34
    self.daysBack = int(origin['daysBack'])

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
      validate_data = self.validate_dataset(data_instance)

      # create coordinate variables, and validate
      coordinate_1    = {'longitude': self.origin_longitude, 'latitude': self.origin_latitude}
      coordinate_2    = {'longitude': coordinates[0], 'latitude': coordinates[1]}
      validate_radius = self.validate_radius(coordinate_1, coordinate_2)

      # validate timeframe
      validate_time = self.validate_date(time)

      # append dataset instance to target list
      if validate_time and validate_data and validate_radius:
        self.target.append( {'id': id, 'coordinates': coordinates, 'magnitude': magnitude, 'time': time, 'location': location} )

  ## validate_dataset: validate subset(s) of given the dataset. The above 'iterator' method,
  #                    implements this method.
  def validate_dataset(self, data_instance):
    try:
      validate(data_instance, jsonschema_data())
      return True
    except Exception, error:
      self.list_error.append( {'class': 'Data_Iterator', 'method': 'validate_dataset', 'msg': error} )
      return False

  ## validate_date: validate if earthquake is within specified number of days.
  #
  #  @current_time, the current time in milliseconds.
  #  @allowed_difference, number of days in milliseconds.
  def validate_date(self, earthquake_time):
    current_time       = int(round(time.time() * 1000))
    difference_allowed = self.daysBack * 86400000
    difference_actual  = current_time - earthquake_time

    if ( difference_actual < difference_allowed ): return {'status': True, 'difference_distance': difference_actual}
    else: return {'status': False, 'difference_distance': difference_actual}

  ## validate_radius: validate given coordinates witin the supplied radius
  def validate_radius(self, p1, p2):
    if get_distance(p1, p2) < self.radius: return True
    else: return False

  ## get_targets: return a list of earthquakes within the supplied parameters.
  def get_targets(self):
    if len(self.target) > 0: return {'data': self.target, 'error': None}
    else:
      self.list_error.append( {'class': 'Data_Iterator', 'method': 'get_targets', 'msg': 'no earthquake instance recorded'} )
      return {'data': None, 'error': self.list_error}

  ## get_largest_target: return largest single earthquake within the supplied parameters.
  def get_largest_target(self):
    if len(self.target) > 0:
      largest_magnitude = max( self.target, key=lambda x:x['magnitude'] )
      return {'data': largest_magnitude, 'error': None}
    else:
      self.list_error.append( {'class': 'Data_Iterator', 'method': 'get_largest_target', 'msg': 'no earthquake instance recorded'} )
      return {'data': None, 'error': self.list_error}
