#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://anilkramakrishna.github.io/'
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

SITELOGO = 'https://anilkramakrishna.github.io/images/anil.jpg'

MENUITEMS = (
    ('Home', 'https://anilkramakrishna.github.io/index.html'),
    ('CV', 'https://anilkramakrishna.github.io/cv.html'),
    )


# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
