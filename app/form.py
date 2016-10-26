from wtforms import Form, BooleanField, StringField, PasswordField, validators, SelectField, SubmitField, TextField
from flask import flash, redirect, url_for, session, render_template, request

class SelectPodcast(Form):
    podcast = SelectField('<h4>Episódio:</h4>', choices=[], coerce=str)
    cast = SubmitField('Selecionar')
    ep_tf = TextField('nome')

class SelectEP(Form):
    ep_cast = SelectField('<h4>PodCast:<h4>', choices=[], coerce=str)
    ep_get = SubmitField('Selecionar')


class Addfeed(Form):
    feed = StringField('FEED')