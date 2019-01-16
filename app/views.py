from flask import flash, redirect, url_for, session, render_template, request
from flask import render_template
from .pycast.feed import Feed
from .pycast.rss import RSS

from app import app


@app.route('/', methods=['GET', 'POST'])
def index():
    error_mensagem = ''
    podcasts_list = list()

    feed = Feed()
    feed.search_file()

    podcasts = feed.select()

    if request.method == 'POST':
        get_feed_url = request.form['url']
        print(get_feed_url)
        print('dddd')
        try:
            if not RSS(get_feed_url).add():
                error_mensagem = 'Error to import'

            podcasts = feed.select()
            for i in range(0, len(podcasts)):
                podcasts_list.append(podcasts[i])
            return render_template('index.html', podcasts_list = podcasts_list, error=error_mensagem)

        except AttributeError:
            error_mensagem = "Erro to import"

    elif feed.number_of_podcasts() == -1:
        return render_template('index.html', podcasts_list = podcasts_list, info=True)

    for i in range(0, len(podcasts)):
        podcasts_list.append(podcasts[i])

    return render_template('index.html', podcasts_list = podcasts_list, error=error_mensagem)

@app.route('/remove/<id>/')
def remove_feed(id):
        feed = Feed()

        feed.remove(id)
        return redirect(url_for('index'))


@app.route('/<id>/')
def episodes(id):
    feed = Feed()

    feed.search_file()

    url_feed = feed.url(id)
    rss = RSS(url_feed)
    episodes_name = rss.search_podcast()
    return render_template('list.html', episodes_name=episodes_name)
