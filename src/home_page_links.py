#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# kashev.rocks
# Kashev Dalmia - kashev.dalmia@gmail.com

from collections import namedtuple


class HomePageLink(namedtuple('HomePageLink', ['name', 'hint',
                                               'color', 'url'])):
    """ The data for a link on the home page of the website. """

    @property
    def svg(self):
        return 'svgs/{}.svg'.format(self.name)


LINKS = [
    HomePageLink('email', 'Email Me', '#DD4B39',
                 'mailto:kashev.dalmia@gmail.com?Subject=Hello!'),

    HomePageLink('resume', 'Resume', '#AAA',
                 '/resume'),

    HomePageLink('github', 'Github', '#555555',
                 'http://github.com/kashev'),

    HomePageLink('linkedin', 'LinkedIn', '#007FB1',
                 'http://linkedin.com/in/kashevdalmia/'),

    HomePageLink('ghost', 'Blog', '#718087',
                 'http://blog.kashevdalmia.com/'),
]
