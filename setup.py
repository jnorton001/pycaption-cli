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
    version='0.1',
    description='Command line caption conversion',
    author='Joe Norton',
    author_email='joey@nortoncrew.com',
    url='https://github.com/jnorton001/pycaption-cli',
    install_requires = dependencies,
    packages = find_packages(),
    include_package_data=True,
    classifiers=[
        'Topic :: Multimedia :: Video',
    ],
)
