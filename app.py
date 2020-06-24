import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
import re

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'dictionary_db'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@dictionary-lopfd.mongodb.net/dictionary_db?retryWrites=true&w=majority'

mongo = PyMongo(app)



@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/browse')
def browse():
    return render_template("browse.html", terms=mongo.db.terms.find())


@app.route('/add_word')
def add_word():
    return render_template('addword.html',
                           speciality=mongo.db.speciality.find())


@app.route('/insert_word', methods=['POST'])
def insert_word():
    terms = mongo.db.terms
    terms.insert_one(request.form.to_dict())
    return redirect(url_for('browse'))

@app.route('/delete_word/<terms_id>')
def delete_word(terms_id):
    mongo.db.terms.remove({'_id': ObjectId(terms_id)})
    return redirect(url_for('browse'))

@app.route('/edit_word/<terms_id>')
def edit_word(terms_id):
    the_term =  mongo.db.terms.find_one({"_id": ObjectId(terms_id)})
    all_specialities =  mongo.db.speciality.find()
    return render_template('editword.html', term=the_term,
                           speciality=all_specialities)


@app.route('/update_word/<terms_id>', methods=["POST"])
def update_word(terms_id):
    terms = mongo.db.terms
    terms.update( {'_id': ObjectId(terms_id)},
    {
        'term':request.form.get('term'),
        'definition':request.form.get('definition'),
        'speciality_name': request.form.get('speciality_name'),
    })
    return redirect(url_for('browse'))

@app.route('/get_specialities')
def get_specialities():
    return render_template('specialities.html',
                           speciality=mongo.db.speciality.find())

@app.route('/edit_speciality/<speciality_id>')
def edit_speciality(speciality_id):
    return render_template('editspeciality.html',
    speciality=mongo.db.speciality.find_one({'_id': ObjectId(speciality_id)}))


@app.route('/update_speciality/<speciality_id>', methods=['POST'])
def update_speciality(speciality_id):
    mongo.db.speciality.update(
        {'_id': ObjectId(speciality_id)},
        {'speciality_name': request.form.get('speciality_name')})
    return redirect(url_for('get_specialities'))

@app.route('/insert_speciality', methods=['POST'])
def insert_speciality():
    speciality_doc = {'speciality_name': request.form.get('speciality_name')}
    mongo.db.speciality.insert_one(speciality_doc)
    return redirect(url_for('get_specialities'))    

@app.route('/delete_speciality/<speciality_id>')
def delete_speciality(speciality_id):
    mongo.db.speciality.remove({'_id': ObjectId(speciality_id)})
    return redirect(url_for('get_specialities'))

@app.route('/add_speciality')
def add_speciality():
    return render_template('addspeciality.html')




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)