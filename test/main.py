import psycopg2
import random
from flask_sqlalchemy import SQLAlchemy
from coinScrapper import Scrapper
from flask import render_template, request, Flask, flash


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:0512rahat@localhost/APP-W05-practice'
db = SQLAlchemy(app)
my_value = ""


class Paragraphs(db.Model):
    __tablename__ = 'paragraphs'
    id = db.Column('id', db.Integer, primary_key=True)
    text = db.Column('text', db.String)

    def __init__(self, id, text):
        self.id = id
        self.text = text


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")


@app.route("/results", methods=['GET', 'POST'])
def hello_world():
    identifier = 'bitcoin'
    parser = Scrapper(currency_name=identifier)
    paragraph_list = parser.scrap_articles()
    id_num = 1
    for record in paragraph_list:
        id_num = random.randint(1, 10000)
        insert = Paragraphs(id_num, record)
        db.session.add(insert)
        db.session.commit()
    return render_template("results.html", identifier=identifier, array=paragraph_list)


if __name__ == "__main__":
    app.run(debug=True)
