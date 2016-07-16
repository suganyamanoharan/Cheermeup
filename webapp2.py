from flask import render_template, request, jsonify
import logging
from flask import Flask
import imageGenerator


app= Flask(__name__)
"""app = create_app(__name__)"""
app.debug = True
logger = logging.getLogger(__name__)

@app.route('/imgs')
def hello(imlist=imageGenerator.weighted_choice(selected_tags)):
    return render_template('images.html', image_list= imlist)




