
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
lib    = mongo.db.stack_libraries

@app.route("/get-all-libraries",methods = ['GET'])
def get_all_libraries():

    libraries = lib.find()
    lib_list = []

    for item in libraries:
        library_obj = {
            "library" : item['library'],
            "logo"    : item['logo']
        }
        lib_list.append(library_obj)
    
    library_list = lib_list

    result_dict = {
        "libraries" : library_list
    }

    return result_dict

@app.route("/get-specific-library",methods=['GET'])
def get_specific_library():

    parent        = request.json['parent']
    library_no    = request.json['number']
    
    libraries = lib.find({"_id.parent":parent,"_id.sno":library_no})
    lib_list = []
    for item in libraries:
        library_obj = {
            "library" : item['library'],
            "link"    : item['github_link']
        }
        lib_list.append(library_obj)
    library_list = lib_list

    result_dict = {
        "libraries" : library_list
    }

    return result_dict


if __name__ == "__main__":

    app.run(debug=True)