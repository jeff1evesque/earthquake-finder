#!/usr/bin/python

## @validator_functions.py
#  This file contains functions needed to  valididate longitude, latitude, radius, and
#    daysBack values.
import requests

## validate_longitude: check if longitude is type 'float', and between [-180, 180].
def validate_longitude(longitude):
  try:
    # check float
    longitude = float(longitude)

    # check bounds
    if -180 <= longitude <= 180: return {'status': True, 'error': None}
    else: return {'status': False, 'error': 'longitude value: ' + str(longitude) + ', must be between [-180, 180]'}
  except ValueError, e:
    return {'status': False, 'error': 'longitude must be an integer, or decimal value.'}

## validate_latitude: check if latitude is type 'float', and between [-90, 90].
def validate_latitude(latitude):
  try:
    # check float
    latitude = float(latitude)

    # check bounds
    if -90 <= latitude <= 90: return {'status': True, 'error': None}
    else: return {'status': False, 'error': 'latitude value: ' + str(latitude) + ', must be between [-90, 90]'}
  except ValueError, e:
    return {'status': False, 'error': 'latitude must be an integer, or decimal value.'}

## validate_radius: check if radius is type 'float', and greater than 0.
def validate_radius(radius):
  try:
    # check float
    radius = float(radius)

    # check bounds
    if radius >= 0: return {'status': True, 'error': None}
    else: return {'status': False, 'error': 'radius value: ' + str(radius) + ', must be greater than, or equal to 0'}
  except ValueError, e:
    return {'status': False, 'error': 'radius must be an integer, or decimal value.'}

## validate_daysBack: check if daysBack is type 'int', and greater than 0.
def validate_daysBack(daysBack):
  try:
    # check int
    daysBack = int(daysBack)

    # check bounds
    if daysBack >= 0: return {'status': True, 'error': None}
    else: return {'status': False, 'error': 'daysBack value: ' + str(daysBack) + ', must be greater than, or equal to 0'}
  except ValueError, e:
    return {'status': False, 'error': 'radius must be an integer value.'}

## validate_dataset_url: check if url is valid, accessible resource.
def validate_dataset_url(url):
  # request (get) given url, store json response content
  r = requests.get(url)
  status_code = r.status_code

  # check status code
  if status_code == 200: return {'status': True, 'error': None}
  else: return {'status': False, 'error': url + ' is not an accessible resource'} 
