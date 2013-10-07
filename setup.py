#!/usr/bin/env python

from distutils.core import setup


setup(
    name='tradeking',
    version='0.1',
    description='Python library for the TradeKing API',
    long_description='Python library for the TradeKing API',
    author='Trey Tabner',
    author_email='trey@tabner.com',
    url='https://github.com/treytabner/python-tradeking',
    py_modules=['tradeking'],
    scripts=['tradeking.py'],
    license='AGPL',
    platforms='any',
    install_requires=[
        'requests',
        'requests-oauthlib',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)
