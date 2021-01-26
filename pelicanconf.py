#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Suibin Sun'
SITENAME = 'Suibin Sun'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Github', 'https://github.com/sun98'),
    # ('Pelican', 'https://getpelican.com/'),
    # ('Python.org', 'https://www.python.org/'),
    # ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
    # ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
    ('Bilibili', 'https://space.bilibili.com/14774330'),
)

DEFAULT_PAGINATION = 10

THEME = './themes/Flex'

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['pelican_plugin-render_math']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Flex config

AUTHOR = "Suibin Sun"
SITEURL = ""
SITENAME = "Suibin Sun's Blog"
SITETITLE = "Suibin Sun"
SITESUBTITLE = "Hello!"
SITEDESCRIPTION = "Suibin's Thoughts and Writings"
SITELOGO = "/images/profile.png"
FAVICON = "/images/favicon.ico"

BROWSER_COLOR = "#00e5ff"

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa"
}

COPYRIGHT_YEAR = 2021

MAIN_MENU = True
