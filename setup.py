#!/usr/bin/env python
import os, sys, glob
from setuptools import setup, find_packages
try:
    from webkit import *
except ImportError:
    print 'Cannot install Kugou :('
    print 'Would you please install package "python-webkit" first?'
    sys.exit()

setup(name = 'Kugou Music',
      description = 'Kugou Music online Player',
      version = '0.1.0',
      maintainer = 'Mutse Young',
      maintainer_email = 'yyhoo2.young@gmail.com',
      url = 'http://mutse.blogbus.com/',
      packages = find_packages(),
      scripts = ['kugou'],
      include_package_data = True,
      package_data = {'': ['*.png', '*.desktop']},
      data_files=[
          ('/usr/local/share/icons/', glob.glob('*.png')),
          ('/usr/local/share/applications/', glob.glob('*.desktop')),
          ],
      license='GNU GPL',
      platforms='linux',
      )