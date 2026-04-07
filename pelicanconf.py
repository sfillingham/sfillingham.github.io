#!/usr/bin/env python
# -*- coding: utf-8 -*-

AUTHOR = 'Sean P. Fillingham'
SITENAME = 'Sean P. Fillingham'
SITEURL = ''
SITESUBTITLE = 'Technical AI Governance · Systems Safety for Frontier AI'

PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Theme
THEME = 'theme'

# URL settings
ARTICLE_URL = 'writing/{slug}/'
ARTICLE_SAVE_AS = 'writing/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Blog settings
DEFAULT_CATEGORY = 'writing'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

# Menu items
MENUITEMS = (
    ('About', '/about/'),
    ('Research', '/research/'),
    ('Writing', '/writing/'),
)

# Index page is custom (landing page)
INDEX_SAVE_AS = 'writing/index.html'

# Static paths
STATIC_PATHS = ['images']

# Feed settings (disable during development)
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Pagination
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Substack URL (used in templates)
SUBSTACK_URL = 'https://substack.com/@seanfillingham'
