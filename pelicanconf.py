#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'gnu-linux.org'
SITENAME = u'gnu-linux.org'
SITEURL = 'http://gnu-linux.org'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

#THEME = 'notmyidea'
THEME = 'simple-bootstrap'
THEME = "static/simple-bootstrap"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# PLUGINS: Sitemap 
PLUGIN_PATH = "plugins"
PLUGINS = ["sitemap"]

# Added by Srikant
SITEMAP = {                                                                 
        'format': 'xml',                                                        
        'priorities': {                                                         
            'articles': 0.5,                                                    
            'indexes': 0.5,                                                     
            'pages': 0.5                                                        
        },                                                                      
        'changefreqs': {                                                        
            'articles': 'daily',                                              
            'indexes': 'daily',                                                 
            'pages': 'daily'                                                  
        }                                                                       
    } 

# Blogroll
LINKS =  (('gnu-linux.org', 'http://gnu-linux.org/'),
    #      ('Python.org', 'http://python.org/'),
    #      ('Jinja2', 'http://jinja.pocoo.org/'),
    #      ('You can modify those links in your config file', '#'),
		)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/srikantpatnaik'),
          ('Google', 'http://plus.google.com/+SrikantPatnaik'),)

DEFAULT_PAGINATION = 25

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Added by Srikant

FILES_TO_COPY = (
   ('extra/robots.txt', 'robots.txt'),
   ('extra/favicon.ico', 'favicon.ico'),
