from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Routes.ruta101b import colinf
from Databases.db import landingdb

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)

# register blueprints
app.register_blueprint(colinf)