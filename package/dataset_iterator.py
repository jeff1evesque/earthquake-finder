#!/usr/bin/python

## @dataset_iterator.py
#  This file iterates a given dataset, and returns a list of dict records, of earthquakes
#      within the supplied parameters (i.e. radius, timeframe).

## Class: Data_Iterator
class Data_Iterator

  ## constructor:
  def __init__(self, dataset):
  self.dataset = dataset
  self.target  = []

  ## iterator: iterate given dataset, and store earthquakes within the specified radius,
  #            and timeframe.
  def iterator(self):

  ## validator: validate subset(s) of given dataset. This is specifically called within
  #             the above 'iterator' method.
  def validator(self):

  ## get_target: returns a list of earthquakes within the supplied parameters.
  def get_target(self):
