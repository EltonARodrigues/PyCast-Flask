#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from xml.etree import ElementTree
from urllib.request import Request
from urllib.request import urlopen
from .models import Feed
from app import app
import feedparser
import requests
import os
import re


class RSS:

    def __init__(self, url):
        self.__file = feedparser.parse(url)

    def add(self):
        episode_title = self.__file.feed.title_detail.value
        img = self.__file.feed.image.href
        return episode_title, self.__verify_img(img)

    def __verify_img(self, cover_url):
        r = requests.head(cover_url)
        if r.status_code == requests.codes.ok:
            return cover_url
        return '../static/img/img_not.png'

    def __count_epsodios(self):
        return self.__file, int((len(self.__file['entries'])))

    def __clear_link(self, mp3):
        re_link = re.search('http.+mp3', mp3)
        return re_link.group(0)

    def search_podcast(self):
        d, epsode_numbers = self.__count_epsodios()
        list_p = list()

        for i in range(epsode_numbers):
            titulo = (d['entries'][i]['title'])
            mp3 = str(d['entries'][i]['enclosures'][0]['href'])
            #description = str(d['entries'][i]['description'])
            list_p.append([titulo, mp3])

        return list_p


class OPML():

    def __init__(self, file):
        self.__file = file

    def get(self):
        self.__file = self.__file.replace("'", '')
        self.__file = self.__file.replace(' ', '')
        with open(self.__file, 'rt') as f:
            tree = ElementTree.parse(f)

        for node in tree.findall('.//outline'):
            url = node.attrib.get('xmlUrl')
            if url:
                try:
                    name, cover = RSS(url).add()
                    feed_row = Feed(name, cover, url)
                    db.session.add(feed_row)
                    db.session.commit()
                except (AttributeError):
                    pass
