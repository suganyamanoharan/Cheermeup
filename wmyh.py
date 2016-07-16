from flask import render_template, request, jsonify
import logging
from flask import Flask, redirect, url_for
from sets import Set

app= Flask(__name__)
"""app = create_app(__name__)"""
app.debug = True
logger = logging.getLogger(__name__)

topics = Set(["food", "landscapes", "tv-series", "cats", "dogs", "pokemon", "travel", "technology", "sports",
              "funny-gifs", "music", "hatching-chicks", "outer-space"])
selected = Set([])

@app.route('/hello', methods=['GET'])
def hello():
    return render_template('hello.html')

@app.route('/wmyh', methods=['GET', 'POST'])        # what makes you happy?
def wmyh():
    if request.method == 'POST':
        if 'done' in request.form.keys():
            print selected
            return redirect(url_for('hello'))
        elif 'search' in request.form.keys():
            new_topic = request.form.get('search')
            topics.add(new_topic)
            selected.add(new_topic)         # put in the DB
        else:
            for item in request.form.keys():
                if item not in selected:
                    selected.add(item)      # put in the DB
                else:
                    selected.remove(item)

    return render_template('wmyh.html', topics=topics, selected=selected)