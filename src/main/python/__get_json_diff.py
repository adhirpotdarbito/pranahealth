import json
import sys
import types

TYPE = 'TYPE'
PATH = 'PATH'
VALUE = 'VALUE'

class Diff(object):
  def __init__(self, first, second):
    self.difference = []
    self.seen = []
    self.check(first, second)

  def check(self, first, second, path=''):
    if second != None:
      if not isinstance(first, type(second)):
        message = '%s - %s, %s' % (path, type(first).__name__, type(second).__name__)
        #self.save_diff(message, TYPE)

    if isinstance(first, dict):
      for key in first:
        # the first part of path must not have trailing dot.
        if len(path) == 0:
          new_path = key
        else:
          new_path = "%s.%s" % (path, key)

        if isinstance(second, dict):
          if second.has_key(key):
            sec = second[key]
          else:
            #  there are key in the first, that is not presented in the second
            #self.save_diff(new_path, PATH)

            # prevent further values checking.
            sec = None

          # recursive call
          if sec != None:
            self.check(first[key], sec, path=new_path)
        else:
          # second is not dict. every key from first goes to the difference
          #self.save_diff(new_path, PATH)
          self.check(first[key], second, path=new_path)

    # if object is list, loop over it and check.
    elif isinstance(first, list):
      for (index, item) in enumerate(first):
        new_path = "%s[%s]" % (path, index)
        # try to get the same index from second
        sec = None
        if second != None:
          try:
            sec = second[index]
          except (IndexError, KeyError):
            # goes to difference
            #self.save_diff('%s - %s' % (new_path, type(item).__name__), TYPE)
            pass
        # recursive call
        self.check(first[index], sec, path=new_path)

    # not list, not dict. check for equality (only if with_values is True) and return.
    else:
      if first != second:
        message = {"parameter_name": path, "parameter_previous_value": first, "parameter_updated_value": second}
        self.save_diff(message, VALUE)
      return

  def save_diff(self, diff_message, type_):
    if diff_message not in self.difference:
      self.seen.append(diff_message)
      self.difference.append((type_, diff_message))


def compare(json_1, json_2):
  diff1 = Diff(json_1, json_2).difference
  diffs = []
  for type, message in diff1:
    newType = 'CHANGED'
    if type == PATH:
      newType = 'REMOVED'
    diffs.append(message)
  return diffs


