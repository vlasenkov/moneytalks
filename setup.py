from setuptools import setup
import sys


if sys.version_info[:2] < (3, 6):
    raise RuntimeError("Python version must be >= 3.6")


setup(name='finam',
      version='0.1',
      description='Unofficial Python interface to Finam services.',
      url='https://github.com/vlasenkov/finam',
      author='Leonid Vlasenkov',
      license='MIT',
      packages=['finam'],
      package_data = {'finam': ['cache/icharts.js']})

