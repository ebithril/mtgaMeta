from mtgsdk import Card

from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request

import os
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/search', methods=['POST'])
def search():
    sets = 'KLD,AER,AKH,HOU,XLN,RIX,DOM'

    searchTerm = request.form['search']
    if not os.path.isdir('cache'):
        os.makedirs('cache')

    cacheFile = 'cache/%s.json' % searchTerm
    if not os.path.isfile(cacheFile):
        cards = Card.where(set=sets).where(name=searchTerm).all()
        with open(cacheFile, 'w') as f:
            data = '['
            for card in cards:
                data += json.dumps(card.__dict__)
                data += ','
            data = data[:-1] + ']'
            f.write(data)

    cards = []
    with open(cacheFile, 'r') as f:
        cards = json.loads(f.read())

    names = []
    for card in cards:
        names.append({'name': card['name'], 'image': card['image_url']})

    return jsonify(names)
