#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import envoy

from PIL import Image


def exists(string):
    """Check to see if file exists"""
    return envoy.run("which %s" % string).status_code == 0

def isimage(file):
    """Check to see if image exists"""
    try:
        Image.open(file)
        return True
    except IOError:
        return False
