#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import sys

from clint import arguments
from clint.textui import puts
from squish.colors import e, s, p
from squish.helpers import exists, isimage
from squish.optimize import Optimize
from squish.statistics import Statistics


class Core:

    def main(self):
        """Starts the script"""
        self._check_dependencies()

        args = arguments.Args()

        if not args.get(0) or not len(args.files) or "--help" in args.flags:
            self._show_help()

        if "--watch" not in args.flags:
            self._iterate_over_files()

    def _iterate_over_files(self):
        """Iterate over the files and apply optimizations"""
        stats = Statistics()

        args = arguments.Args()

        for file in args.files:

            if isimage(file):
                before_size = stats.calculate_before_optimization(file)

                puts("%s %s" % (
                    e("==>"),
                    os.path.basename(file))
                )

                if "--lossy" in args.flags:
                    Optimize.lossy(file)
                if "--lossless" in args.flags:
                    Optimize.lossless(file)
                after_size = stats.calculate_after_optimization(file)

                puts("%s %s (%s)" % (
                    p("<=="),
                    os.path.basename(file),
                    s(after_size) if after_size < before_size else after_size
                ))

        stats.show_statistics()

    def _check_dependencies(self):
        """Check to see if all the dependencies have been installed"""
        imgmin = exists('imgmin')
        image_optim = exists('image_optim')

        if not imgmin or not image_optim:
            puts(p('Dependencies have not been installed:'))

            message = 'imgmin - https://github.com/rflynn/imgmin'
            message = s('✓ ' + message) if imgmin else e('✗ ' + message)
            puts(message)

            message = 'image_optim - http://rubygems.org/gems/image_optim'
            message = s('✓ ' + message) if image_optim else e('✗ ' + message)
            puts(message)

            sys.exit(0)

    def _show_help(self):
        """Show the help system"""
        puts(e("Usage: %s [options] <file/folder>" % sys.argv[0]))

        puts(p("--help        ") + "Show the help system")
        puts(p("--lossy       ") + "Apply a lossy optimization on the image(s)")
        puts(p("--lossless    ") + "Apply a lossless optimization on the image(s)")
        puts(p("--watch       ") + "Watch a folder and apply optimizations straight up")

        sys.exit(0)
