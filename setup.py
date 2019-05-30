#!/usr/bin/env python

import sys

from setuptools import find_packages, setup

if sys.version_info < (3, 7, 0):
    raise Exception("This project is incompatible with Python < 3.7.")

setup(
    name="indydatascot",
    version="0.0.1",
    description="Making stats that relate to Scottish independence easy to access.",
    author="Andy Herd",
    author_email="herdingdata@users.noreply.github.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)
