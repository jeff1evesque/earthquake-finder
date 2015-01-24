#!/usr/bin/python

## @validator_request.py
#  This file validates user supplied GPS coordinates (longitude, latitude), and
#      parameters (radius, days back).
from package.validator_functions import validate_longitude, validate_latitude, validate_radius, validate_daysBack

## validate_request: validate received request parameters.
def validate_request( origin ):
  list_error = []

  # validation logic
  validate_longitude = validate_longitude( origin['longitude'] )
  validate_latitude  = validate_latitude( origin['latitude'] )
  validate_radius    = validate_radius( origin['radius'] )
  validate_daysBack  = validate_daysBack( origin['daysBack'] )

  # return error
  if len(list_error) > 0:
    return { 'status': False, 'error': list_error }
  else:
    return { 'status': True, 'error': None }
