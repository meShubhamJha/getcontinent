import os
from setuptools import setup

setup(name='getcontinent',
      version='1.0.0',
      description='This module can help you to get the continent of different countries',
      url='https://github.com/meShubhamJha/getconti',
      author='Shubham Jha',
      author_email='sjha0090@gmail.com',
      license='MIT',
      packages=['getconti'],
      python_requires='>3.5.2',
      install_requires=['pandas'],
      classifiers = [
      "Programming Language :: Python :: 3",
      "Operating System :: OS Independent"],
      include_package_data=True,
      zip_safe=False)