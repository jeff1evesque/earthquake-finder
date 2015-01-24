#!/usr/bin/python

## @json_scraper.py
#  This file contains functions needed to  valididate longitude, latitude, radius, and
#    daysBack values.

# validate_longitude: check if longitude is type 'float', and between [-180, 180].
def validate_longitude():
  try:
    # check float
    float(origin['longitude'])

    # check bounds
    if -180 <= origin['longitude'] <= 180: return {'status': True, 'error': None}
    else: return {'status': False, 'error': 'longitude value: ' . + str(origin['longitude']) + ', must be between [-180, 180]'}
  except ValueError, e:
    return {'status': False, 'error': 'longitude must be an integer, or decimal value.'}

# validate_latitude: check if latitude is type 'float', and between [-90, 90].
def validate_latitude():
  try:
    # check float
    float(origin['latitude'])

    # check bounds
    if -90 <= origin['latitude'] <= 90: return {'status': True, 'error': None}
    else: return {'status': False, 'error': 'latitude value: ' . + str(origin['latitude']) + ', must be between [-90, 90]'}
  except ValueError, e:
    return {'status': False, 'error': 'latitude must be an integer, or decimal value.'}

# validate_radius: check if radius is type 'float', and greater than 0.
def validate_radius():
  try:
    # check float
    float(origin['radius'])

    # check bounds
    if origin['radius'] >= 0: return {'status': True, 'error': None}
    else: return {'status': False, 'error': 'radius value: ' . + str(origin['radius']) + ', must be greater than, or equal to 0'}
  except ValueError, e:
    return {'status': False, 'error': 'radius must be an integer, or decimal value.'}

# validate_daysBack: check if daysBack is type 'int', and greater than 0.
def validate_daysBack():
  try:
    # check int
    int(origin['daysBack'])

    # check bounds
    if origin['daysBack'] >= 0: return {'status': True, 'error': None}
    else: return {'status': False, 'error': 'daysBack value: ' . + str(origin['daysBack']) + ', must be greater than, or equal to 0'}
  except ValueError, e:
    return {'status': False, 'error': 'radius must be an integer value.'}
