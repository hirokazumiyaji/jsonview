#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(name='jsonview',
      version='0.1',
      description='json view for django',
      author='Hirokazu Miyaji',
      author_email='hirokazu.miyaji@gmail.com',
      keywords=['json', 'django'],
      url='https://github.com/hirokazumiyaji/jsonview',
      packages=['jsonview'],
      license='MIT',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'License :: OSI Approved :: MIT License',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
      ],
)
