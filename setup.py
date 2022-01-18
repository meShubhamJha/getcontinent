import os
from setuptools import setup

setup(name='getcontinents',
      version='0.1.0',
      description='This module can help you to get the continent of different countries',
      url='https://github.com/meShubhamJha/getconti',
      author='Shubham Jha',
      author_email='sjha0090@gmail.com',
      license='MIT',
      packages=['getconti'],
      python_requires='>3.5.2',
      install_requires=['pandas',"os"],
      classifiers = [
      "Programming Language :: Python :: 3",
      "Licence :: OSI Approved :: MIT License",
      "Operating System :: OS Independent"]
      zip_safe=False)