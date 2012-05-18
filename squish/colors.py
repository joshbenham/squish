#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from clint.textui import colored


# Color: Error
def e(s):
  return colored.red(s)

# Color: Success
def s(s):
  return colored.green(s)

# Color: Primary
def p(s):
  return colored.cyan(s)
