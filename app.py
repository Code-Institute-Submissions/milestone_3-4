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
    return render_template("index.html", terms=mongo.db.terms.find())

@app.route('/add_word')
def add_word():
    return render_template('addword.html',
                           speciality=mongo.db.speciality.find())


@app.route('/insert_word', methods=['POST'])
def insert_word():
    terms = mongo.db.terms
    terms.insert_one(request.form.to_dict())
    return redirect(url_for('index'))

@app.route('/delete_word/<terms_id>')
def delete_word(terms_id):
    mongo.db.terms.remove({'_id': ObjectId(terms_id)})
    return redirect(url_for('index'))

@app.route('/edit_word/<terms_id>')
def edit_word(terms_id):
    the_term =  mongo.db.terms.find_one({"_id": ObjectId(terms_id)})
    all_specialities =  mongo.db.speciality.find()
    return render_template('editword.html', term=the_term,
                           speciality=all_specialities)



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)