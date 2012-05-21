#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# vim: sw=2 ts=2

import envoy


class Optimize:

  @staticmethod
  def lossy(file):
    envoy.run("imgmin %s %s" % (file, file))

  @staticmethod
  def lossless(file):
    envoy.run("image_optim %s" % file)
