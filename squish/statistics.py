#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os

from PIL import Image
from clint.textui import puts
from squish.colors import p, s


class Statistics:

    # Total files
    files = 0

    # File types
    pngs = 0
    jpgs = 0
    gifs = 0

    # Total size
    preSize = 0
    postSize = 0

    def pre(self, file):
        self._baseCalculations(file)
        self.preSize += self._getFileSize(file)

    def post(self, file):
        self.postSize += self._getFileSize(file)

    def show(self):
        puts(p("Statistics:"))

        puts("Total Files: %s (PNGs %s/JPGs %s/GIFs %s)" % (
            s(self.files),
            s(self.pngs),
            s(self.jpgs),
            s(self.gifs)
        ))
        puts("Original File/Folder Size: %s" % s(round(self.preSize, 2)))
        puts("New File/Folder Size: %s" % s(round(self.postSize, 2)))
        puts("Savings of: %s%%" % s(self._getSavings()))

    def _getSavings(self):
        return round(100 - ((100 * self.postSize) / self.preSize), 2)

    def _getFileSize(self, file):
        return os.stat(file).st_size / 1024.0

    def _baseCalculations(self, file):
        self.files += 1
        stream = Image.open(file)

        if stream.format == "PNG":
            self.pngs += 1

        if stream.format == "JPG":
            self.jpgs += 1

        if stream.format == "GIF":
            self.gifs += 1
