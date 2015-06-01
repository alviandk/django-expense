#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup
from expense import VERSION
import os

files = ["templates/admin/expense/expense/*",
         "static/expense/images/*.*",
         "static/expense/js/*.*",
         "static/expense/js/flot/*.*",
         "static/expense/css/*.*",
         "static/expense/css/cupertino/*.*",
         "static/expense/css/cupertino/images/*.*",]

setup(name='django-expense',
      version=VERSION.replace(' ', '-'),
      description='A simple personal/family expense tracker application for Django.',
      author=u'Tibor Tóth',
      author_email='szunyog@gmail.com',
      url='https://bitbucket.org/szunyog/django-expense/',
      packages=['expense','expense.templatetags'],
      package_data = {'expense' : files },
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Framework :: Django'],
      )
