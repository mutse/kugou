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
      scripts = ['kugou/kugou'],
      include_package_data = True,
      data_files=[
          ('/usr/local/share/icons/', glob.glob('data/kugou.png')),
          ('/usr/local/share/applications/', glob.glob('data/kugou.desktop')),
          ],
      license='GNU GPL',
      platforms='linux',
)

