squish
==========

[Josh Benham](http://joshbenham.net)'s Image Optimization tool
[![Build Status](https://secure.travis-ci.org/joshbenham/squish.png?branch=master)](http://travis-ci.org/joshbenham/squish)

Overview
--------

A simple tool to optimize images for the web. Can use lossy and lossless optimizations or a combination of both.

Dependencies
------------

Currently **squish** has two dependencies that will have to get installed seperately.

1. [imgmin](https://github.com/rflynn/imgmin) to handle smart lossy image optimizations.
2. [image_optim](http://rubygems.org/gems/image_optim) to handle lossless image optimizations

Instructions
------------
```sh
# grab the repo
$ git clone git@github.com:joshbenham/squish.git

# change into the squish directory
$ cd squish

# install python requirements
$ pip install --requirement requirements.txt

# symlink it to your bin directory
$ ln -s squish_r ~/bin/squish
```

Also make sure that your ~/bin directory is in your environment path.

Usage
-------

Lossless compression
```sh
# on a file
$ squish_r --lossless file.jpg

# on a folder
$ squish_r --lossless folder/
```

Lossy compression
```sh
# on a file
$ squish_r --lossy file.jpg

# on a folder
$ squish_r --lossy folder/
```
