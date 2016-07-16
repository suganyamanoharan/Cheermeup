from flask import render_template, request, jsonify
import logging,os
import imageGenerator
from flask import Flask, redirect, url_for
from flask import g
import sqlite3

app= Flask(__name__)
"""app = create_app(__name__)"""
app.debug = True
logger = logging.getLogger(__name__)

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

topics = ["food", "landscapes", "tv series", "cats", "dogs", "pokemon", "travel", "technology", "sports",
              "funny gifs", "music", "hatching chicks", "outer space"]
selected = []

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


@app.route('/home/<name>')
def home(name="Default"):
    return render_template('abcd.html', name=name)

@app.route('/wmyh', methods=['GET', 'POST'])        # what makes you happy?
def wmyh():
    if request.method == 'POST':
        if 'done' in request.form.keys():
            selected_topics = []
            for item in request.form.keys():
                if item != 'done':
                    ## put in the DB
                    selected_topics.append(item)
            return redirect(url_for('hello'))
        else:
            new_topic = request.form.get('search')
            topics.append(new_topic)
            selected.append(new_topic)
            return render_template('wmyh.html', topics=topics, selected=selected)

    return render_template('wmyh.html', topics=topics)
