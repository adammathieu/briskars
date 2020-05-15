import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ta-gueule-c-est-magique'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite3:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
