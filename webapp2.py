from flask import render_template, request, jsonify
import logging
from flask import Flask

import sys

app= Flask(__name__)
"""app = create_app(__name__)"""
app.debug = True
logger = logging.getLogger(__name__)

def selected_topics(topics):
    print topics

@app.route('/home/<name>')
def home(name="Default"):
    return render_template('abcd.html', name=name)

@app.route('/wmyh', methods=['GET', 'POST'])        # what makes you happy?
def wmyh():
    topics = ["food", "landscapes", "tv series", "cats", "dogs", "pokemon", "travel", "technology", "sports",
            "funny gifs", "music", "hatching chicks", "outer space"]
    if request.method == 'POST':
        selected_topics(request.form)
    elif request.method == 'GET':
        return render_template('wmyh.html', topics=topics)



