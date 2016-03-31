#!/usr/bin/env python

# Remove .egg-info directory if it exists, to avoid dependency problems with
# partially-installed packages (20160119/dphiffer)

import os, sys
from shutil import rmtree

cwd = os.path.dirname(os.path.realpath(sys.argv[0]))
egg_info = cwd + "/mapzen.whosonfirst.meta.egg-info"
if os.path.exists(egg_info):
    rmtree(egg_info)

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read()
version = open("VERSION").read()

setup(
    name='mapzen.whosonfirst.git',
    namespace_packages=['mapzen', 'mapzen.whosonfirst', 'mapzen.whosonfirst.git'],
    version=version,
    description='Simple Python utilities for working with Who\'s On First files and Git',
    author='Mapzen',
    url='https://github.com/mapzen/py-mapzen-whosonfirst-git',
    install_requires=[
        ],
    dependency_links=[
        ],
    packages=packages,
    scripts=[
        'scripts/wof-git-changed'
        ],
    download_url='https://github.com/whosonfirst/py-mapzen-whosonfirst-git/releases/tag/' + version,
    license='BSD')
