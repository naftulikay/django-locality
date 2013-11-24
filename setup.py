#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="django-locality",
    version="0.2.2",
    url='https://github.com/rfkrocktk/django-locality',
    license='AGPL',
    description='Countries and territories, made usable.',
    author='Naftuli Tzvi Kay',
    author_email='rfkrocktk@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    package_data={
    '': ['locality/fixtures/*.json']
    },
    install_requires=[
        'Django>=1.3.0',
        'django-localflavor',
        'setuptools'
    ],
    zip_safe=False,
)
