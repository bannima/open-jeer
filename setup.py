#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(name='open-jeer',
      version='0.1.0',
      description='Deep Learning Library for Joint Extraction of Entities and Relations',
      author='Enguo Zhou',
      author_email='zhouenguo@126.com',
      url='https://github.com/bannima/open-jeer',
      license='MIT',
      install_requires=[
          'numpy', 'scipy', 'torch', 'transformers',
          'six', 'h5py', 'Pillow',
          'scikit-learn', 'metric-learn'],
      extras_require={
          'docs': ['sphinx', 'sphinx_rtd_theme'],
      },
      packages=find_packages(),
      keywords=[
          'Joint Extraction of Entities and Relations',
          'Named Entitiy Recognition',
          'Relation Extraction',
      ])

