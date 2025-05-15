from setuptools import setup, Extension

c_mod = Extension(
	name='c_extension',
	sources=['c_extension.c']
)

setup(
	name='insecure-flask-app',
	version='0.1.0',
	description='Flask app with C extension',
	ext_modules=[c_mod],
	py_modules=['app'],
)

