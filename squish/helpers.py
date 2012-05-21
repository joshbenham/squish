#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# vim: sw=2 ts=2

import envoy

from PIL import Image


def exists(string):
  return envoy.run("which %s" % string).status_code == 0

def isimage(file):
  try:
    Image.open(file)
    return True
  except IOError:
    return False
