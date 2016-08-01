from wtforms import Form, BooleanField, StringField, PasswordField, validators, SelectField, SubmitField
from flask import flash, redirect, url_for, session, render_template, request

class SelectPodcast(Form):
    podcast = SelectField(u'<legend>Episódio: </legend>', choices=[], coerce=str)
    cast = SubmitField('Selecionar')

class SelectEP(Form):
    ep_cast = SelectField(u'<legend>PodCast:', choices=[], coerce=str)
    ep_get = SubmitField('Selecionar')

class Addfeed(Form):
    feed = StringField('FEED')