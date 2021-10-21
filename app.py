from flask import Flask, render_template, request, jsonify, make_response
import os
#import database.database_config as db
#from dotenv import load_dotenv
from flask.helpers import send_file

#load_dotenv()

app = Flask(__name__, static_folder="client/build/static", template_folder="client/build")

@app.route('/')
def root():
    return render_template('index.html')

@app.route("/welcome_msg")
def get_current_msg():
        return {"msg": "Welcome folks"}


@app.route("/appjobs")
def get_jobtable():
    return {"tableData": [
        { 'title': 'Sr. Software Eng.', 'company': 'Intel', 'appdt': '09/01/21',},
        { 'title': 'Software Eng.', 'company': 'Amd', 'appdt': '09/10/21',},
        { 'title': 'Jr. Software Eng.', 'company': 'Microsoft', 'appdt': '09/05/21',},
        { 'title': 'Software Eng.', 'company': 'Amazon', 'appdt': '08/20/21',},
      ],
      "tableColumns":  [
        {'Header': 'Title', 'accessor': 'title'},
        {'Header': 'Company', 'accessor': "company"},
        {'Header': "Application Date",'accessor': "appdt"}
        ],
      }

@app.route("/contacts")
def get_conttable():
    return {"tableData": [
        { 'contact': 'Helen Smith', 'companies': 'Intel', 'match': '5',},
        { 'contact': 'Mark Wright', 'companies': 'Amd', 'match': '3',},
        { 'contact': 'James Jeff', 'companies': 'Amazon', 'match': '1',},
      ],
      "tableColumns":  [
        {'Header': 'Contact', 'accessor': 'contact'},
        {'Header': 'Companies', 'accessor': "companies"},
        {'Header': "Job Matches",'accessor': "match"}
        ],
      }

@app.route("/companies")
def get_comptable():
    return {"tableData": [
        {'company':'AMD', 'contact':'Mark Watson', 'match':'5',},
        {'company':'Intel', 'contact':'Helen Smith', 'match':'3',},
        {'company':'Microsoft', 'contact':'Helen Smith', 'match':'1',},
        {'company':'Amazon', 'contact':'James Jeff', 'match':'1',},

      ],
      "tableColumns":  [
          {'Header': 'Company', 'accessor': "company"},
          {'Header': 'Contacts', 'accessor': 'contact'},
          {'Header': "Job Matches",'accessor': "match"}
        ],
      }

@app.route("/skills")
def get_skilltable():
    return {"tableData": [
        {'skill':'Java', 'pro':'8', 'match':'5',},
        {'skill':'Python', 'pro':'7', 'match':'3',},
        {'skill':'MySQL', 'pro':'8', 'match':'1',},
        {'skill':'C/C++', 'pro':'6', 'match':'1',},
        {'skill':'AWS', 'pro':'7', 'match':'3',},
        {'skill':'Angular', 'pro':'2', 'match':'4',},
      ],
      "tableColumns":  [
          {'Header': 'Skill', 'accessor': "skill"},
          {'Header': 'Proficiency (1-10)', 'accessor': 'pro'},
          {'Header': "Job Matches",'accessor': "match"}
        ],
      }



print("Starting server")

if __name__ == '__main__':
    
#    if os.environ["DB_CREATE_SEED"] == "True" or os.environ["DB_CREATE_SEED"] == "true":
#        print("")
#        print("Creating tables and seeing dummy data")
#        print("")
#        db.main()

    # Will set port to 5000 on local machine, but allow Heroku to bind on deployment.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
