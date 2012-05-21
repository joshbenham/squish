#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# vim: sw=2 ts=2

import sys

from clint import args
from clint.textui import puts, indent
from squish.colors import e, s, p
from squish.helpers import exists, isimage
from squish.optimize import Optimize
from squish.statistics import Statistics


class Core:

  def main(self):
    self._check_dependencies()

    if not args.get(0) or not len(args.files) or "--help" in args.flags:
      self._show_help()

    if "--watch" not in args.flags:
      self._iterate_over_files()


  # Iterate over the files and apply optimizations
  def _iterate_over_files(self):

    stats = Statistics()

    for file in args.files:
      
      if isimage(file):

        stats.pre(file)

        if "--lossy" in args.flags:
          Optimize.lossy(file)

        if "--lossless" in args.flags:
          Optimize.lossless(file)
      
        stats.post(file)

    if "--stats" in args.flags:
      stats.show()



  # Check to see if all the dependencies have been installed
  def _check_dependencies(self):

    imgmin = exists('imgmin')
    image_optim = exists('image_optim')

    if not imgmin or not image_optim:
      puts(p('Dependencies have not been installed:'))

      with indent(3):
        message = 'imgmin - https://github.com/rflynn/imgmin'
        message = s('✓ ' + message) if imgmin else e('✗ ' + message)
        puts(message)

        message = 'image_optim - http://rubygems.org/gems/image_optim'
        message = s('✓ ' + message) if image_optim else e('✗ ' + message)
        puts(message)

      sys.exit(1)


  # Show the use the help system
  def _show_help(self):

    puts(e("Usage: %s [options] <file/folder>" % sys.argv[0]))

    with indent(3):
      puts(p("--help        ") + "Show the help system")
      puts(p("--lossy       ") + "Apply a lossy optimization on the image(s)")
      puts(p("--lossless    ") + "Apply a lossless optimization on the image(s)")
      puts(p("--watch       ") + "Watch a folder and apply optimizations straight up")
      puts(p("--stats       ") + "Show stats of the optimizations")
    
    sys.exit(1)
