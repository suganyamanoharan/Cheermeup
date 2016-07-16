from flask import render_template, request, jsonify
import logging
from flask import Flask


app= Flask(__name__)
"""app = create_app(__name__)"""
app.debug = True
logger = logging.getLogger(__name__)



@app.route('/home/<name>')
def hello(name="Default"):
    return render_template('abcd.html', name=name )



