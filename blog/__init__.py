from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(error):
    return {"message": "URL is not available"}
