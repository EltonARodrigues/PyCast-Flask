from flask import render_template
from flask import flash, redirect, url_for, session, render_template, request
from .XMLCSV.XMLdata import XMLdata
from .XMLCSV.csv_import import CSVfeed
import webbrowser

from app import app

url_feed = None
pod_selected = None
@app.route('/', methods=['GET', 'POST'])
def register():
    global url_feed
    global pod_selected

    ep_choices = list()
    ep_tf = list()

    CSV = CSVfeed()
    CSV.file_csv()
    view = CSV.select()

    for i in range(0, len(view)):
        ep_tf.append(view[i])

    if 'podselect' in request.form:
        pod_selected = request.form['pod_name']
        if pod_selected != None:
            CSV.file_csv()

            url_feed = CSV.get_url(pod_selected)

            XML = XMLdata(url_feed)
            ep_names = XML.list_pod(XML.feed_in())

        for ep in range(0, len(ep_names)):
            ep_choices.append(ep_names[ep])

        return render_template('feed.html', ep_tf = ep_tf, ep_get = ep_choices)

    if 'epselect' in request.form:
        XML = XMLdata(url_feed)
        ep_selected = request.form['ep_name']
        print(ep_selected)
        print(pod_selected)
        teste = XML.search_pod(XML.feed_in(),ep_selected,pod_selected)
        #message = ('Donwload Complete - '+  ep_selected)
        webbrowser.open(teste)
        return render_template('feed.html', ep_tf = ep_tf, ep_get = ep_choices, message = message)

        return render_template('feed.html')
    if 'addfeed' in request.form:
        try:
            get_feed = request.form['addf']

            if CSV.verify(get_feed) == True:
                error_mensagem = 'Feed já existente!'
                return render_template('feed.html', ep_tf = ep_tf, error = error_mensagem)
            else:
                XMLdata(get_feed).add_feed()

                view = CSV.select()
                for i in range(0, len(view)):
                    ep_tf.append(view[i])

                return render_template('feed.html', ep_tf = ep_tf)

        except AttributeError:

            if ep_choices == None:
                return render_template('feed.html', error = 'Link invalido ou em branco ')

            else:
                return render_template('feed.html', ep_tf = ep_tf, error = 'Link invalido ou em branco')

    if 'delfeed' in request.form:
        ep_selected = request.form['pod_name']
        CSV.remove(CSV.get_id(ep_selected))
        print("tete:{}".format(ep_choices))

        if ep_choices == None:
            return render_template('feed.html')

        else:
            return render_template('feed.html', ep_tf = ep_tf, ep_get = ep_choices)

    return render_template('feed.html', ep_tf = ep_tf)
