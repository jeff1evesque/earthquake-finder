#!/usr/bin/python

## @validator_request.py
#  This file validates user supplied GPS coordinates (longitude, latitude), and
#      parameters (radius, days back).
from package.validator_functions import validate_longitude, validate_latitude, validate_radius, validate_daysBack

## validate_request: validate received request parameters.
def validate_request( origin ):
  list_error = []

  # Validate Longitude
  try:
    # check float
    float(origin['longitude'])

    # check bounds
    if -180 <= origin['longitude'] <= 180: pass
    else: self.list_error.append('longitude value: ' . + str(origin['longitude']) + ', must be between [-180, 180]')
  except ValueError, e:
    self.list_error.append('longitude must be an integer, or decimal value.')

  # Validate Latitude
  try:
    # check float
    float(origin['latitude'])

    # check bounds
    if -90 <= origin['latitude'] <= 90: pass
    else: self.list_error.append('latitude value: ' . + str(origin['latitude']) + ', must be between [-90, 90]')
  except ValueError, e:
    self.list_error.append('latitude must be an integer, or decimal value.')

  # Validate Radius
  try:
    # check float
    float(origin['radius'])

    # check bounds
    if origin['radius'] >= 0: pass
    else: self.list_error.append('radius value: ' . + str(origin['radius']) + ', must be greater than, or equal to 0')
  except ValueError, e:
    self.list_error.append('radius must be an integer, or decimal value.')

  # Validate DaysBack
  try:
    # check int
    int(origin['daysBack'])

    # check bounds
    if origin['daysBack'] >= 0: pass
    else: self.list_error.append('daysBack value: ' . + str(origin['daysBack']) + ', must be greater than, or equal to 0')
  except ValueError, e:
    self.list_error.append('radius must be an integer value.')

  # return error
  if len(list_error) > 0:
    return { 'status': False, 'error': list_error }
  else:
    return { 'status': True, 'error': None }
