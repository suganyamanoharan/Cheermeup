from flask import render_template, request, jsonify
import logging
from flask import Flask, redirect, url_for

app= Flask(__name__)
"""app = create_app(__name__)"""
app.debug = True
logger = logging.getLogger(__name__)

topics = ["food", "landscapes", "tv series", "cats", "dogs", "pokemon", "travel", "technology", "sports",
              "funny gifs", "music", "hatching chicks", "outer space"]
selected = []

@app.route('/hello', methods=['GET'])
def hello():
    return render_template('hello.html')

@app.route('/wmyh', methods=['GET', 'POST'])        # what makes you happy?
def wmyh():
    if request.method == 'POST':
        if 'done' in request.form.keys():
            selected_topics = []
            for item in request.form.keys():
                if item != 'done':
                    print "PUT PUT PUT"+str(item)
                    selected_topics.append(item)
            return redirect(url_for('/'))
        else:
            new_topic = request.form.get('search')
            topics.append(new_topic)
            selected.append(new_topic)
            return render_template('wmyh.html', topics=topics, selected=selected)

    return render_template('wmyh.html', topics=topics)
