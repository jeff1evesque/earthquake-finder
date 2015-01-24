#!/usr/bin/python

## @jsonschema_definitions.py
#  This file contains various jsonschema definitions.

## jsonschema_request(): contains the jsonschema for supplied parameters.
def jsonschema_request():
  schema = {
    'type': 'object',
    'properties': {
      'gps_longitude': {
        'type': 'number',
        'minLength': 1
      },
      'gps_latitude': {
        'type': 'number',
        'minLength': 1
      },
      'gps_radius': {
        'type': 'number',
        'minLength': 1
      },
      'daysBack': {
        'type': 'integer',
        'minLength': 1
      },
    }
  }
  return schema

## jsonschema_data(): contains the jsonschema for each iterated element of the
#                     geojson dataset.
def jsonschema_data():
  schema = {
    'type': 'object',
    'properties': {
      'id': {
        'type': 'string',
        'minLength': 1
      },
      'coordinates': {
        'type': 'array',
         'items': {
           'type': 'number',
           'minLength': 1,
         },
         'minItems': 2,
         'maxItems': 3
      },
      'magnitude': {
        'type': 'number',
        'minLength': 1
      },
      'time': {
        'type': 'integer',
        'minLength': 1
      },
      'location': {
        'type': 'string',
        'minLength': 1
      }
    }
  }
  return schema
