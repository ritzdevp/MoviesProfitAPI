from flask import Flask, request, jsonify
from flask import render_template, redirect
import functools, json
import time
from datetime import datetime

app = Flask(__name__)
