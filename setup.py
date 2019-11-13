#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="django-locality",
    version="0.2.4",
    url='https://github.com/naftulikay/django-locality',
    license='MIT',
    description='Countries and territories, made usable.',
    author='Naftuli Kay',
    author_email='me@naftuli.wtf',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    package_data={
    '': ['locality/fixtures/*.json']
    },
    install_requires=[
        'django',
        'django-localflavor',
        'setuptools'
    ],
    zip_safe=False,
)
