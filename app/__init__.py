import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config_default')

logging.basicConfig(level=app.config.get('LOG_LEVEL', logging.DEBUG))
db = SQLAlchemy(app)

from app import views, models

