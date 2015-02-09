#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sergio Ugalde Marcano'
SITENAME = 'Blog de CAS'
SITEURL = ''

PATH = 'content'
STATIC_PATHS=['images']

TIMEZONE = 'America/Mexico_City'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LINKS = (('Pelican', 'http://getpelican.com/'),
         )

# Social widget
SOCIAL = (('facebook','https://www.facebook.com/profile.php?id=100001791786184'),
          ('github','https://github.com/serch037'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
THEME = "/home/sergio/pelican-themes/mg"
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
DIRECT_TEMPLATES = ('index', 'categories', 'archives', 'search', 'tipue_search')
TIPUE_SEARCH_SAVE_AS = 'tipue_search.json'
TYPOGRIFY = True
SUMMARY_MAX_LENGTH = 25

