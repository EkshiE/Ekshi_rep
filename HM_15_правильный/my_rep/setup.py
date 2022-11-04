""" A setuptools base setup modul """

from os import path
from setuptools import setup
from setuptools import find_namespace_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf8') as f:
    long_description = f.read()

setup(
    name='my_pgs',
    version='01.00',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://git.my_rep',
    package_dir={'': 'src'},
    packages=find_namespace_packages(where='src'),
    python_requires='>= 3.6, < 4.0',
    install_requires=[
        'flask',
        'PrettyTable'
    ]
)
