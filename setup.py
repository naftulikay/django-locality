from setuptools import setup, find_packages

setup(
	name = "django-locality",
	version = "0.0.1-SNAPSHOT",
	url = 'http://blog.tkassembled.com/locality',
	license = 'AGPL',
	description = 'Countries and territories, made usable.',
	author = 'TK Kocheran',
	packages = find_packages('src'),
	package_dir = {'': 'src'},
	install_requires = [
		'Django>=1.3.0',
		'setuptools'
	],
)
