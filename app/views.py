from flask import redirect, url_for, session, render_template, request
from flask import render_template
from .helpers import RSS
from .models import Feed
from app import app
from . import db


@app.route('/', methods=['GET', 'POST'])
def index():
    error_mensagem = ''
    info = False

    if request.method == 'POST':
        url_feed = request.form['url']
        try:
            verify_duplicate = Feed.query.filter_by(url=url_feed).scalar()

            if verify_duplicate == None:
                name, cover = RSS(url_feed).add()
                feed_row = Feed(name, cover, url_feed)
                db.session.add(feed_row)
                db.session.commit()
            else:
                error_mensagem = "Duplicate feed"

        except AttributeError:
            error_mensagem = "Erro to import"

    count_feeds = Feed.query.filter_by().count()
    if count_feeds == 0:
        info=True

    query = db.select([Feed.id,Feed.name,Feed.path_cover])
    podcasts = db.session.execute(query).fetchall()

    return render_template('index.html',
                            podcasts_list = podcasts,
                            error=error_mensagem, info=info)

@app.route('/remove/<int:id>/')
def remove(id):
    Feed.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/<int:id>/')
def episodes(id):
    query = Feed.query.filter_by(id=id).first()
    rss = RSS(query.url)
    episodes_name = rss.search_podcast()
    return render_template('list_ep.html', episodes_name=episodes_name, cover=query.path_cover)
