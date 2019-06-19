#!/usr/bin/env python
import os
from setuptools import setup, find_packages

README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                           'README.md')

dependencies = [
    'pycaption'
]

setup(
    name='pycaption-cli',
    version='0.2',
    description='Command line caption conversion',
    author='Joe Norton',
    author_email='joey@nortoncrew.com',
    url='https://github.com/Cielo24/pycaption-cli.git',
    install_requires=dependencies,
    packages=find_packages(),
    include_package_data=True,
    entry_points=dict(
        console_scripts=['pycaption=pycapcli.caption_converter:main']),
)
