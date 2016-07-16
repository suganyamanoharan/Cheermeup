from flask import render_template, request, jsonify
import logging,os
import imageGenerator
from flask import Flask, redirect, url_for
from flask import g
import sqlite3
from sets import Set
import json

app= Flask(__name__)
"""app = create_app(__name__)"""
app.debug = True
logger = logging.getLogger(__name__)

topics = Set(["food", "landscapes", "tv-series", "cats", "dogs", "pokemon", "travel", "technology", "sports",
              "funny-gifs", "music", "hatching-chicks", "outer-space"])
selected = Set([])

#DAtabase
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(APP_ROOT, 'cheermeup.db')

@app.before_request
def before_request():
    g.db = sqlite3.connect(DATABASE)

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

'''REDUNDANT - handled down in /'''
@app.route('/imgs')
def generatePaths(imlist=imageGenerator.weighted_choice({"dogs":10,"cats":10})):
    return render_template('images.html', image_list= imlist)

topics = Set(["food", "landscapes", "tv-series", "cats", "dogs", "pokemon", "travel", "technology", "sports",
                  "funny-gifs", "music", "hatching-chicks", "outer-space"])
selected = Set([])

@app.route('/hello', methods=['GET'])
def hello():
    return render_template('hello.html')

@app.route('/')
def index():
    imlist=imageGenerator.weighted_choice(getTags())
    print("List" + str(imlist))
    return render_template('index.html',image_list=imlist)

def getTags():
    tags = g.db.execute("SELECT tagname,feedback FROM tags").fetchall()
    dict = {}
    for element in tags:
        dict[str(element[0])] = element[1]
    return dict

@app.route('/likes-handler', methods=['POST'])
def handleLikesAndDislikes():
    tag = request.json['tag']
    value = request.json['value']
    if value == 'dislike':
        pass #-1
    elif value == 'dislike':
        pass #increment count
    return json.dumps({'status':'OK'})

@app.route('/wmyh', methods=['GET', 'POST'])        # what makes you happy?
def wmyh():
    if request.method == 'POST':
        if 'done' in request.form.keys():
            # add everything selected to the db
            return redirect(url_for('index'))
        elif 'search' in request.form.keys():
            new_topic = request.form.get('search')
            topics.add(new_topic)
            selected.add(new_topic)
        else:
            for item in request.form.keys():
                if item not in selected:
                    selected.add(item)
                else:
                    selected.remove(item)

    nothingSelected = len(selected) == 0
    return render_template('wmyh.html', topics=topics, selected=selected, nothingSelected =nothingSelected)
