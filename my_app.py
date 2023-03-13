from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:secret@192.168.31.10/metro"
db.init_app(app)


class change_way(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Change = db.Column(db.String(64), nullable=False)
    Line = db.Column(db.String(64), nullable=False)


class balance_card(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Phone = db.Column(db.String(64), nullable=False)
    Code = db.Column(db.String(64), nullable=False)
    Balance = db.Column(db.String(64), nullable=False)
    Last_into = db.Column(db.String(64), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def hello_world():
    return 'Hello, World!'


app.run(host="0.0.0.0")