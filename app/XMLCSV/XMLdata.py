import os
import feedparser
import urllib
import urllib.request
from .csv_import import CSVfeed


class XMLdata:

    def __init__(self,url):
        self.url = url
        self.d = feedparser.parse(url)
        self.link_p = self.d.feed.title_detail.base
        self.title_p = self.d.feed.title_detail.value
        self.url_site = self.d.feed.link

    def add_feed(self):

        CSV = CSVfeed()
        CSV.new_feed(self.title_p,self.link_p)

    def feed_in(self):
        n_epsodes = int((len(self.d['entries'])))
        return self.d, n_epsodes


    def clear_link(self, mp3):
        re_link = re.search('http.+mp3',mp3)
        return re_link.group(0)

    def list_pod(self,feed):
        d, n_epsodes = feed
        list_p = list()

        for i in range(n_epsodes):
            titulo = (d['entries'][i]['title'])
            list_p.append(titulo)

        return list_p

    def search_pod(self, feed, search, name_pod):
        d, n_epsodes = feed
        list_q = {}
        quant_episodes = 0
        error_search = 0

        for i in range(n_epsodes):
            titulo = (d['entries'][i]['title'])

            if str.find(str.upper(titulo), str.upper(search)) != -1:

                search_value = i
                list_q[int(quant_episodes)] = i
                quant_episodes += 1

        mp3 = str(d['entries'][search_value]['enclosures'])
        name = str(d['entries'][search_value]['title'])

        mp3 = mp3.split('.mp3')[0]
        mp3 = mp3.split('http://')[-1]

        if str.find(mp3, 'http://') != 0:
            mp3 = 'http://' + mp3

        if str.find(mp3, '.mp3') == -1:
            mp3 = mp3 + '.mp3'

        return mp3
        '''html = urllib.request.urlopen(mp3).read()
        name = name + '.mp3'

        #remove / filename
        if str.find(name, ','):
            name = name.replace('/','')

        d = ('PodCast/' + name_pod + '/')

        if not os.path.exists(d):
            os.makedirs(d)

        arq = open(d + name, 'wb')
        arq.write(html)
        arq.close()'''
