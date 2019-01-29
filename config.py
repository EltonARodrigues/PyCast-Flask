# config.py
import os


class Config(object):
    """
    Common configurations
    """
    SECRET_KEY = os.urandom(24)
    #SQLALCHEMY_DATABASE_URI = 'mysql://root:root@db/pycastdb'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@172.21.0.2/pycastdb'

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}