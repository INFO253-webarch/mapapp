#!/usr/bin/env python
import shelve
from subprocess import check_output
import flask
from flask import request, Flask, render_template, jsonify, abort, redirect
from os import environ

from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map


import os
import sys
import json
import hashlib

app = flask.Flask(__name__)
GoogleMaps(app)
app.debug = True

db = shelve.open("map.db")

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route("/map",methods=['POST'])
def mapview():
	mapData = request.form.get('mappoints')
	mapData = eval(mapData)
	print mapData

    # creating a map in the view
	sndmap = Map(
		identifier="sndmap",
		lat= 39.5,
		lng= -98.35,
		zoom = 5,
		style = "height: 100%; width: 100%; top:0; left:0; position:absolute; z-index:200",
		markers= {'http://maps.google.com/mapfiles/ms/icons/green-dot.png': mapData}
	)
	return render_template('map.html', sndmap=sndmap)

if __name__ == "__main__":
    app.run()