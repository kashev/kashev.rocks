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
        return open('src/static/img/icons/{}.svg'.format(self.name)).read()


LINKS = [
    HomePageLink('home', 'My Other Website', '#30A848',
                 'http://kashevdalmia.com/'),

    HomePageLink('email', 'Email Me', '#DD4B39',
                 'mailto:kashev.dalmia@gmail.com?Subject=Hello!'),

    HomePageLink('resume', 'Resume', '#AAA',
                 '/resume'),

    HomePageLink('github', 'Github', '#555555',
                 'http://github.com/kashev'),

    HomePageLink('lastfm', 'Last.fm', '#D51007',
                 'http://www.last.fm/user/aerovai'),

    HomePageLink('instagram', 'Instagram', '#125688',
                 'http://www.instagram.com/kashev'),

    HomePageLink('tumblr', 'Tumblr', '#2C4762',
                 'http://blog.kashev.rocks'),

    HomePageLink('ghost', 'Blog', '#718087',
                 'http://blog.kashevdalmia.com/'),
]
