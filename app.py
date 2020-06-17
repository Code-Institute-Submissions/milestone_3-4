import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'dictionary_db'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@dictionary-lopfd.mongodb.net/dictionary_db?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", diagnosis=mongo.db.diagnosis.find())

@app.route('/add_word')
def add_word():
    return render_template('addword.html',
                           speciality=mongo.db.speciality_name.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)