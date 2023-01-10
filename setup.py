# -*- coding: utf-8 -*-

# Ruckus Cloud MSP - Python program to extract from API and update influx database.

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='rkscldmsp_grafana',
    version='0.1.0',
    description='Ruckus MSP Cloud monitoring with Grafana',
    long_description=readme,
    author='Karthikeyan Krish',
    author_email='karthikeyan.m@commscope.com',
    url='https://github.com/indhradhanush',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

#EOL