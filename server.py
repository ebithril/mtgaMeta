from mtgsdk import Card

from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/search', methods=['POST'])
def search():
    sets = 'KLD,AER,AKH,HOU,XLN,RIX,DOM'

    names = []
    cards = Card.where(set=sets).where(name=request.form['search']).all()
    for card in cards:
        names.append({'name': card.name, 'image': card.image_url})

    return jsonify(names)
