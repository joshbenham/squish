#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os

from PIL import Image
from clint.textui import puts
from squish.colors import s


class Statistics:

    """Total files"""
    files = 0

    """File types"""
    pngs = 0
    jpgs = 0
    gifs = 0

    """Total size"""
    pre_size = 0
    post_size = 0

    def calculate_before_optimization(self, file):
        """Gather stats before optimizations are applied"""
        size = self.get_file_size(file)
        self.get_base_calculations(file)
        self.pre_size += size
        return round(size, 2)

    def calculate_after_optimization(self, file):
        """Gather stats after optimizations are applied"""
        size = self.get_file_size(file)
        self.post_size += self.get_file_size(file)
        return round(size, 2)

    def show_statistics(self):
        """Show statistics of the optimizations"""
        puts("\nFiles: %s (PNGs %s/JPGs %s/GIFs %s)" % (
            s(self.files),
            s(self.pngs),
            s(self.jpgs),
            s(self.gifs)
        ))
        puts("Original Size: %s" % s(round(self.pre_size, 2)))
        puts("New Size: %s" % s(round(self.post_size, 2)))
        puts("Savings: %s%%" % s(self._get_savings()))

    def get_file_size(self, file):
        """Get the file size of the given file"""
        return os.stat(file).st_size / 1024.0

    def get_base_calculations(self, file):
        """Get base calculations of the file"""
        self.files += 1
        stream = Image.open(file)

        if stream.format == "PNG":
            self.pngs += 1

        if stream.format == "JPG" or stream.format == "JPEG":
            self.jpgs += 1

        if stream.format == "GIF":
            self.gifs += 1

    def _get_savings(self):
        """Calculate the savings of the optimizations"""
        return round(100 - ((100 * self.post_size) / self.pre_size), 2)
