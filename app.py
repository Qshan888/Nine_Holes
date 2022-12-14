# * Hello world flask app.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

from config.environment import db_URI


# ? Instantiate flask
# ? __name__ is going to be a different value depending on
# ? where you run flask from. If you run this directly,
# ? it will be '__main__'
app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = db_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

ma = Marshmallow(app)

bcrypt = Bcrypt(app)

from controllers import golfs, categories, users

app.register_blueprint(golfs.router, url_prefix="/api")

app.register_blueprint(categories.router, url_prefix="/api")

app.register_blueprint(users.router, url_prefix="/api")
