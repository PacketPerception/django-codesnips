#! /usr/bin/env python

"""
Distutils setup file for codesnips
"""

from setuptools import setup, find_packages
from codesnips import __version__

setup(
    name='codesnips',
    version=__version__,
    packages=find_packages(),
    install_requires=[],

    # Metadata
    author='Brian',
    author_email='brian(at)packetperception.org',
    description='Django code snippets',
    long_description="""
    Snippets of code that are useful with Django.
    """,
    license='MIT',
    url='https://github.com/PacketPerception/django-codesnips',
    keywords='Django',
)
