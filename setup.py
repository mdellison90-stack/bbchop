#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script for BBChop package."""

from setuptools import setup, find_packages
import os

# Read the long description from README
readme_path = os.path.join(os.path.dirname(__file__), 'README')
with open(readme_path, 'r') as f:
    long_description = f.read()

setup(
    name='bbchop',
    version='0.1.0',
    description='Bisection algorithm which works on intermittent bugs',
    long_description=long_description,
    long_description_content_type='text/plain',
    author='Ealdwulf Wuffinga',
    license='GPL-2.0-or-later',
    url='https://github.com/mdellison90-stack/bbchop',
    
    # Package discovery
    package_dir={'': 'BBChop/source'},
    py_modules=[
        'BBChop',
        'cse',
        'dag',
        'dagRead',
        'entropy',
        'evidence',
        'likelihoods',
        'listUtils',
        'miscMath',
        'numberType',
        'persistentMemo',
        'skipProbability',
        'testLog',
    ],
    
    # Entry point for the command-line script
    scripts=['BBChop/source/bbchop'],
    
    # Python version requirement
    python_requires='>=2.6',
    
    # Optional dependencies
    extras_require={
        'fast': ['mpmath'],
    },
    
    # Classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Testing',
    ],
)
