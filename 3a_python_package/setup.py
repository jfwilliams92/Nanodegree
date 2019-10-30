from setuptools import setup

setup(
   name='distributions',
   version='1.0',
   description='Module for using statistical distributions',
   author='James Williams',
   author_email='jfw@g.clemson.edu',
   packages=['distributions'],  #same as name
   install_requires=['numpy'], #external packages as dependencies
)