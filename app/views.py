from flask import render_template
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from flask import flash, redirect, url_for, session, render_template, request
from .form import SelectPodcast, SelectEP, Addfeed
from .XMLCSV.XMLdata import XMLdata
from .XMLCSV.csv_import import CSVfeed

from app import app

url_feed = ''
pod_selected = None

@app.route('/', methods=['GET', 'POST'])
def register():
    global pod_selected
    global url_feed
    add = Addfeed(request.form)
    cast = SelectPodcast(request.form)
    ep_get = SelectEP(request.form)

    choices_pod = list()
    ep_choices = list()

    CSV = CSVfeed()
    CSV.file_csv()
    view = CSV.select()

    for i in range(0, len(view)):
        choices_pod.append((view[i],view[i]))
    cast.podcast.choices = choices_pod

    if 'podselect' in request.form:
        pod_selected =  cast.podcast.data

        if pod_selected != None: 
            CSV.file_csv()
            
            url_feed = CSV.get_url(pod_selected)

            XML = XMLdata(url_feed)
            ep_names = XML.list_pod(XML.feed_in())

        for ep in range(0, len(ep_names)):
            ep_choices.append((ep_names[ep],ep_names[ep]))
        ep_get.ep_cast.choices = ep_choices


        return render_template('feed.html',cast = cast, ep_get = ep_get, add = add)
    
    if 'epselect' in request.form:
        XML = XMLdata(url_feed)
        ep_selected =  ep_get.ep_cast.data  
        print(ep_selected)
        XML.search_pod(XML.feed_in(),ep_selected,pod_selected)


        return render_template('feed.html',cast = cast, ep_get = ep_get, message = ('Donwload Complete - '+  ep_selected), add = add)

    if 'addfeed' in request.form:
        get_feed = add.feed.data
        if CSV.verify(get_feed) == True:
            error_mensagem = 'Já Existente!'
            return render_template('feed.html',cast = cast, error = error_mensagem, add = add)
        else:
            XMLdata(get_feed).add_feed()
            #teste
            view = CSV.select()
            for i in range(0, len(view)):
                choices_pod.append((view[i],view[i]))
                cast.podcast.choices = choices_pod
            #######
            return render_template('feed.html',cast = cast, add = add)

    return render_template('feed.html', cast = cast, add = add)
