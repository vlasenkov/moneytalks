from setuptools import setup
import sys


if sys.version_info[:2] < (3, 6):
    raise RuntimeError("Python version must be >= 3.6")


setup(name='moneytalks',
      version='0.1',
      description='Stock data manipulation library',
      url='https://github.com/vlasenkov/moneytalks',
      author='Leonid Vlasenkov',
      license='MIT',
      packages=['moneytalks'],
      package_data = {'moneytalks': ['finam/icharts.js']})

