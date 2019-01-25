from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from app import db


class Feed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    path_cover = db.Column(db.String(255))
    url = db.Column(db.String(255), nullable=False)

    def __init__(self, name, path_cover, url):
        self.name = name
        self.path_cover = path_cover
        self.url = url