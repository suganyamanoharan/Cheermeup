from flask import render_template, request, jsonify
import logging,os
import imageGenerator
import textToImage
from flask import Flask, redirect, url_for
from flask import g
import sqlite3
from sets import Set
import json
from werkzeug.utils import secure_filename
import personalImages

ALLOWED_EXTENSIONS = set([ 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/images/personal')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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

def deleteTags():
     	print ("DELETED TAGS")
  	g.db.execute('DELETE FROM tags')
  	g.db.commit()
  
def insertTags(item):
      	print ( "INSERT INTO TAGS ('tagname') VALUES ("+str(item)+")")
  	g.db.execute('INSERT INTO TAGS (tagname) VALUES (?)',[item])
  	g.db.commit()

def updateIncrementTags(item):
         print ( "UPDATE tags SET feedback = feedback + 1 WHERE tagname="+str(item))
         g.db.execute('UPDATE tags SET feedback = feedback + 1 WHERE tagname=?',[item])
         g.db.commit()
 
def updateDecrementTags(item):
         print ( "UPDATE tags SET feedback = feedback - 1 WHERE tagname="+str(item))
         g.db.execute('UPDATE tags SET feedback = feedback - 1 WHERE tagname=?',[item])
         g.db.commit()
 


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
@app.route('/')
def index():
    plist = personalImages.pullPersonalPictures()
    imlist=imageGenerator.weighted_choice(getTags())
    print("List" + str(imlist))
    return render_template('index.html',image_list=imlist, plist = plist)


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
         updateDecrementTags(tag)
    elif value == 'like':
         updateIncrementTags(tag)
    return json.dumps({'status':'OK'})


@app.route('/wmyh', methods=['GET', 'POST'])        # what makes you happy?
def wmyh():
    if request.method == 'POST':
        if 'done' in request.form.keys():
            deleteTags()
 	    for item in selected:
 		insertTags(item)
            return redirect(url_for('index'))           # potentially a different url
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
    nothingSelected = len(selected) == 0
    return render_template('wmyh.html', topics=topics, selected=selected, nothingSelected =nothingSelected)


@app.route('/condition')
def condition():
    return render_template('condition.html')

@app.route('/helloworld')
def thanks():
    return render_template('thankyou.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/uploadimages', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file',
                                    filename=filename))
    return render_template('upload.html')


def uploadImage(textString):
	print ( "Text to image done for " + textString)
	textToImage.textToImage(textString)
