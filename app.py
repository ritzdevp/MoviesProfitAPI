from flask import Flask, request, jsonify
from flask import render_template, redirect
import functools, json
import time
from datetime import datetime

app = Flask(__name__)

listofmovies = []
class MovieInfo:
	def __init__(self, name, start, end):
		self.name = name
		self.start = start
		self.end = end

@app.route('/get_max_profit_API', methods = ['GET'])
def get_max_profit_API():
	def compareEnds(movieA, movieB):
		return movieA.end - movieB.end

	