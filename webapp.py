from flask import render_template, request, jsonify
import logging
import flask

app = create_app(__name__)
app.debug = True
logger = logging.getLogger(__name__)


class InvalidUsage(Exception):
    status_code = 400
    # the above code was an example

    def __init__(self, message, status_code=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code



@app.route('/<url>', methods=['GET/POST'])
def function():
    return render_template('abcd.html', variable_name_used_in_html_file=variable_got_from_function )



