#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# vim: sw=2 ts=2

from clint.textui import colored


def e(s):
  """Color: Error"""
  return colored.red(s)

def s(s):
  """Color: Success"""
  return colored.green(s)

def p(s):
  """Color: Primary"""
  return colored.cyan(s)
