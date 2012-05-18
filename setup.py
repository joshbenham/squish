# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
  readme = f.read()

with open('LICENSE') as f:
  license = f.read()

setup(
  name='squish',
  version='0.0.1',
  description='Simple image optimization tool',
  long_description=readme,
  author='Josh Benham',
  author_email='joshbenham@gmail.com',
  url='https://github.com/joshbenham/squish',
  license=license,
  packages=find_packages(exclude=('tests', 'docs'))
)
