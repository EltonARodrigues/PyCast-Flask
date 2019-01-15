#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from .feed import Feed
from urllib.request import Request
from urllib.request import urlopen
import feedparser
import os
import re


class RSS:

    def __init__(self, url):
        self.url = url
        self.__file = feedparser.parse(url)
        self.__episode = self.__file.feed.title_detail.base
        self.__episode_title = self.__file.feed.title_detail.value
        self.__img = self.__file.feed.image.href

    def add(self):
        return Feed().new(self.__episode_title, self.__episode, self.url, self.__img)

    def __count_epsodios(self):
        return self.__file, int((len(self.__file['entries'])))

    def download(self, name, url_mp3):
        req = Request(self.__clear_link(url_mp3),
                      headers={'User-Agent': 'Mozilla/5.0'})

        html = urlopen(req).read()

        name = name + '.mp3'

        # remove/filename
        if str.find(name, ','):
            name = name.replace('/', '')

        d = ('PodCast/' + self.__episode_title + '/')

        if not os.path.exists(d):
            os.makedirs(d)

        arq = open(d + name, 'wb')
        arq.write(html)
        arq.close()

    def __clear_link(self, mp3):
        re_link = re.search('http.+mp3', mp3)
        return re_link.group(0)

    def search_podcast(self):
        d, epsode_numbers = self.__count_epsodios()
        list_p = list()

        for i in range(epsode_numbers):
            titulo = (d['entries'][i]['title'])
            mp3 = str(d['entries'][i]['enclosures'][0]['href'])
            list_p.append([titulo, mp3])

        return list_p