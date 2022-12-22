#!/usr/bin/env python3

from setuptools import find_packages, setup

setup(
    name='openwrt-test',
    version='1',
    url='https://github.com/vunaman/sendmail.git',
    author='An Vu',
    author_email='an.vu.k18bku@hcmut.edu.vn',
    description='OpenWRT Test for Python package',
    packages=find_packages(),    
    install_requires=['python3'],
    py_modules=[
        'sendmail',
    ],
)