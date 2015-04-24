"""
(c) Copyright 2014. All Rights Reserved.

qball module setup and package.
"""

from setuptools import setup

setup(
    name='qball',
    author='Matt Ferrante',
    author_email='mferrante3@gmail.com',
    description='Python integration for qball',
    license='(c) Copyright 2014. All Rights Reserved.',
    packages=['qball'],
    install_requires=['httplib2 >= 0.8'],
    setup_requires=['httplib2'],
    version='1.1.0',
    url="https://github.com/ferrants/qball-python",
    keywords = ['locking', 'resource locking', 'webservice'],
)
