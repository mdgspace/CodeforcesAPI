#!/usr/bin/env python
# encoding: utf-8
from flask import Flask, jsonify
from scraper import scrape

app = Flask(__name__)

@app.route('/scrape/<string:q>', methods = ['GET'])
def scrape_data(q):
    data = scrape(q)
    return jsonify(data)

app.run(debug=True)