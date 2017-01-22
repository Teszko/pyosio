#!/usr/bin/env python
import os
from setuptools import setup, find_packages


setup(
    name='pyosio',
    version='0.5',
    description='A python wrapper for OpenSensors API API',
    url='https://github.com/tzano/pyosio',
    author='Tahar',
    author_email='taharz.dev@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='IoT',
    packages=find_packages(),
    install_requires=['requests','sseclient','pyyaml'],
)
