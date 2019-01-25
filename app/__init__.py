from sqlalchemy_utils import database_exists, create_database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import app_config
from flask import Flask

db = SQLAlchemy()

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config['development'])
app.config.from_object('config.Config')

if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
    create_database(app.config['SQLALCHEMY_DATABASE_URI'])

db.init_app(app)

migrate = Migrate(app, db)
from app import views, models



