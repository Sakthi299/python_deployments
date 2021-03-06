
# Import necessary modules
import os
#[1]
import logging
#[2]
from flask import Flask, jsonify, request, make_response, session,json

app = Flask(__name__)

# app configs
app.config['MONGO_URI'] = #[3]

mongo = PyMongo(app)
book  = mongo.db  #[4] 

@app.route("/add-new-contact",methods = #[5]
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

    return #[6]

@app.route("/get-all-contacts",methods = #[7])
def get_all_contacts():

    #[8]

    result_dict = {
        "Contacts" : contact_list
    }

    return result_dict

@app.route("/get-specific-contact",methods=['GET'])
def get_specific_contact():

    #[9]
    
    contact = #[10]
    contact_list = []
    for item in contact:
        contact_obj = {
            "Name"      : #[11]
            "Mobile"    : 
        }
        contact_list.append(#[12])

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

    book.update_one({"name":name},{#[13])

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

    #[14]

    result_dict = {
        "Status" : "Contact deleted Successfully"
    }

    return result_dict

if __name__ == "__main__":

    #[15]