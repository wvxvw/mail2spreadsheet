#!/usr/bin/env python

import sys
from setuptools import setup

setup(
    name='mail2spreadsheet',
    version='1.0',
    description='Filter and forward some info from GMail to GoogleSpreadsheet',
    author='Oleg Sivokon',
    author_email='olegsivokon@gmail.com',
    url='https://github.com/wvxvw/mail2spreadsheet',
    packages=['mail2spreadsheet'],
    package_dir={'mail2spreadsheet': 'src/mail2spreadsheet'},
    package_data={'mail2spreadsheet': ['etc/*.*']},
    scripts=['scripts/mail2spreadsheet'],
    install_requires = [
        'oauth2client >= 4.1.2',
        # If this is not installed, you will have to install GCC and
        # other tools needed to compile C code :(
        #
        # For Debian and Ubuntu, the following command will ensure
        # that the required dependencies are installed:
        # 
        # $ sudo apt install build-essential libssl-dev libffi-dev python-dev
        # 
        # For Fedora and RHEL-derivatives, the following command will
        # ensure that the required dependencies are installed:
        # 
        # $ sudo dnf install gcc libffi-devel python-devel openssl-devel
        'PyOpenSSL >= 17.3.0',
        'gspread >= 0.6.2',
        'configparser >= 3.5.0',
    ],
)
