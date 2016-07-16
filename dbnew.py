from flask import g,Flask,render_template,jsonify
import sqlite3
import json
import os


app= Flask(__name__)
"""app = create_app(__name__)"""
app.debug = True
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(APP_ROOT, 'cheermeup.db')


@app.before_request
def before_request():
    g.db = sqlite3.connect(DATABASE)

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/')
def emails():
    tags = g.db.execute("SELECT tagname,feedback FROM tags").fetchall()
    dict = {}
    for element in tags:
        dict[str(element[0])] = element[1]
    print dict
    return render_template('index.html')
