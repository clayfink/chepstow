from setuptools import setup

__author__ = 'Cash Costello'
__email__ = 'cash.costello@jhuapl.edu'
__version__ = '0.0.1-dev'

setup(
    name='chepstow',
    version=__version__,
    description='This library is only a test',
    long_description=open('README.md').read(),
    author=__author__,
    author_email=__email__,
    license='BSD',
    packages=['chepstow'],
    keywords='',
    classifiers=[
    ],
    install_requires=[
    ],
    python_requires='>=3.5',
)