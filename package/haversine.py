#!/usr/bin/python

## @haversine.py
#  This file contains the necesary methods needed to compute the distance between
#      two GPS coordinate points (longitude, latitude).
import math

## degrees_to_radians: converts supplied value from degrees, to radians.
def degrees_to_radians(deg):
  return deg * (math.pi / 180)
