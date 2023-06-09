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


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")


@app.route("/change_data", methods=["POST"])
def change_data():
    bd = change_way.query.order_by(change_way.Id).all()
    return render_template("change_data.html", bd=bd)


@app.route("/balance_auto", methods=["POST"])
def change_data():
    return render_template("/balance_auto")


@app.route("/metro_data", methods=["POST"])
def metro_data():
    code = request.form.get("sms")
    phone = request.form.get("phone")
    if ((balance_card.query.filter_by(Code=int(code)).first()) and (balance_card.query.filter_by(Phone=phone).first())):  # Если данные существуют
        if (balance_card.query.filter_by(Code=int(code)).first()) == (balance_card.query.filter_by(Phone=phone).first()):  # Если равны
            item = balance_card.query.filter_by(Code=int(code)).first()
            balance = item.Balance
            station = item.Last_into
            return render_template("/metro_data.html", balance=balance, station=station)
        else:
            return render_template("/fall.html")
    else:
        return render_template("/fall.html")


app.run(host="0.0.0.0")