#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import envoy


class Optimize:

    @staticmethod
    def lossy(file):
        """Run imgmin on the given file"""
        envoy.run("imgmin %s %s" % (file, file))

    @staticmethod
    def lossless(file):
        """Run image_optim on the given file"""
        envoy.run("image_optim %s" % file)
