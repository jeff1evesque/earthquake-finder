#!/usr/bin/python

## @haversine.py
#  This file contains the necesary methods needed to compute the distance between
#      two GPS coordinate points (longitude, latitude).
from math import radians, cos, sin, asin, sqrt

## get_distance: computes the distance between two GPS coordinate points using the
#                haversine formula.
#
#  Note: this function returns the haversine distance in meters.
def get_distance(p1, p2):
  # radius of the earth (meters)
  radius = 6378137

  # convert decimal degrees to radians
  lon1, lat1, lon2, lat2 = map(radians, [p1['longitude'], p1['latitude'], p2['longitude'], p2['latitude']])

  # haversine formula
  dlon = lon2 - lon1
  dlat = lat2 - lat1
  a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
  c = 2 * asin(sqrt(a))

  # return distance
  d = radius * c
  return d
