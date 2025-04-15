#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'anil'
SITENAME = u'Anil Ramakrishna'
SITEURL = 'https://anilkramakrishna.github.io/'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images', 'pdfs']

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

SITELOGO = 'https://anilkramakrishna.github.io/images/anil.jpg'

MENUITEMS = (
    ('Home', 'https://anilkramakrishna.github.io/index.html'),
    ('CV', 'https://anilkramakrishna.github.io/cv.html'),
    )

# Social widget
# SOCIAL = (('scholar', 'https://scholar.google.com/citations?user=KNu_OpsAAAAJ&hl=en'),
#          ('linkedin', 'https://www.linkedin.com/in/anilramakrishna'),
#          ('github', 'http://github.com/anilkram'))

#DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

"""
HTML for sidebar
<li><a href="https://scholar.google.com/citations?user=KNu_OpsAAAAJ&hl=en" target="_blank"><img src="./images/scholar.svg" style="width:36px;height:32.5px;"></a></li>
        <li><a href="https://www.linkedin.com/in/anilramakrishna" target="_blank"><img src="./images/linkedin.svg" style="width:36px;height:32.5px;"></a></li>
        <li><a href="http://github.com/anilkram" target="_blank"><img src="./images/github.svg" style="width:36px;height:32.5px;"></a></li>
"""

THEME = "Flex/"
