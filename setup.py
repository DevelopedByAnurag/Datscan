try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md", 'r') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = [line.strip() for line in f.readlines()]

setup(
   name='DatScan',
   version='1.0.0',
   description="An automated data scraper and  Analyser tool",
   long_description=long_description,
   url='https://github.com/DevelopedByAnurag/Datscan/',
   packages=['/'],
   install_requires=requirements
)
