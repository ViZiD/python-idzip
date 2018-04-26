#!/usr/bin/python
from setuptools import setup, find_packages

VERSION = "0.3"

setup(
    name = "python-idzip",
    version = VERSION,
    packages=find_packages(),
    description = 'DictZip - Random Access gzip files',
    author = 'Rik Faith',
    maintainer= 'Dan Bauman',
    maintainer_email='dan@bauman.space',
    license='MIT',
    url = 'https://github.com/bauman/python-idzip',
    download_url = 'https://github.com/bauman/python-idzip/%s.tar.gz' %(VERSION),
    classifiers = [
                       'License :: OSI Approved :: MIT License',
                       'Operating System :: OS Independent',
                       'Programming Language :: Python',
                       'Programming Language :: Python :: 2',
                       'Programming Language :: Python :: 3',
                   ],
    scripts=['bin/idzip']
)
