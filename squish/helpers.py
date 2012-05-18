#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import envoy

def exists(string):
  return envoy.run("which %s" % string).status_code == 0
