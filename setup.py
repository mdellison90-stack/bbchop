#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script for BBChop package."""

from setuptools import setup

setup(
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
)
