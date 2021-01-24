
# Import necessary modules
import os
from decouple import config
import logging
from flask_pymongo import PyMongo
from flask import Flask, jsonify, request, make_response, session,json


# Local Import
#from controllers import *
#import response_utils
app = Flask(__name__)

# app configs
app.config['MONGO_URI'] = config('MONGO_URI')

mongo = PyMongo(app)
book  = mongo.db['telephone-registry'] 

@app.route("/add-new-contact",methods = ['POST'])
def add_new_contacts():

    name  = request.json['name']
    phone = request.json['phone']
    place = request.json['place']

    contact_obj = {
        "name"      : name,
        "phone"     : phone,
        "place"     : place
    }
       
    book.insert_one(contact_obj)

    result_dict = {
        "Status" : "Contact Inserted Successfully"
    }

    return result_dict

@app.route("/get-all-contacts",methods = ['GET'])
def get_all_contacts():

    contacts = book.find()
    contact_list = []

    for item in contacts:
        contact_obj = {
            "name"      : item['name'],
            "mobile"    : item['phone'],
            "place"     : item['place']
        }
        contact_list.append(contact_obj)

    result_dict = {
        "Contacts" : contact_list
    }

    return result_dict

@app.route("/get-specific-contact",methods=['GET'])
def get_specific_contact():

    name = request.json['name']
    
    contact = book.find({"name":name})
    contact_list = []
    for item in contact:
        contact_obj = {
            "Name"      : item['name'],
            "Mobile"    : item['phone']
        }
        contact_list.append(contact_obj)

    result_dict = {
        "Contacts" : contact_list
    }

    return result_dict

@app.route("/update-specific-contact" ,methods=['PUT'])
def update_specific_contact():

    name  = request.json['name']
    mobile = request.json['phone']
    
    result_dict = {
        "name" : name
    }

    book.update_one({"name":name},{"$set":{"phone":mobile}})

    result_dict = {
        "Status" : "Contact updated Successfully"
    }

    return result_dict

@app.route("/delete-specific-contact" , methods=['DELETE'])
def delete_specific_contact():

    name  = request.json['name']
    
    result_dict = {
        "name" : name
    }

    book.delete_one(result_dict)

    result_dict = {
        "Status" : "Contact deleted Successfully"
    }

    return result_dict

if __name__ == "__main__":

    app.run(debug=True)