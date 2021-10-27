from flask import Flask, render_template, request, jsonify, make_response
import os
import database.database_config as db
from dotenv import load_dotenv
from flask.helpers import send_file
from flask import send_from_directory 

# flag for standing up database locally
standup_db = False

load_dotenv()

app = Flask(__name__, static_folder="client/build/static", template_folder="client/build")


@app.route('/')
def root():
    return render_template('index.html')

# This fixes the favicon log error. If we use a favicon later, we can remove this
@app.route("/favicon.ico")
def favicon():
    return "", 200

@app.route("/welcome_msg")
def get_current_msg():
        return {"msg": "Welcome folks"}

@app.route("/appjobs")
def get_jobtable():

    userid = db.getUserForMock()
    val =  db.getTableApplications(userid)

    return {"tableData": 
        val,
            "tableColumns":  [
        {'Header': 'Title', 'accessor': 'title'},
        {'Header': 'Company', 'accessor': "company"},
        {'Header': "Application Date",'accessor': "appdt"}
        ],
      }

@app.route("/contacts")
def get_conttable():
    
    userid = db.getUserForMock()
    val =  db.getTableContacts(userid)
    print(val)

    return {"tableData": val,
      "tableColumns":  [
        {'Header': 'Contact', 'accessor': 'contact'},
        {'Header': 'Companies', 'accessor': "company"},
        {'Header': "Job Matches",'accessor': "jobCount"}
        ],
      }

@app.route("/companies")
def get_comptable():

    userid = db.getUserForMock()
    val =  db.getTableContacts(userid)
    return {"tableData": val, 
      "tableColumns":  [
          {'Header': 'Company', 'accessor': "company"},
          {'Header': 'Contacts', 'accessor': 'contact'},
          {'Header': "Job Matches",'accessor': "jobCount"}
        ],
      }

@app.route("/skills")
def get_skilltable():

    userid = db.getUserForMock()
    val =  db.getTableSkills(userid)
    return {"tableData": val,
      "tableColumns":  [
          {'Header': 'Skill', 'accessor': "skill"},
          {'Header': 'Proficiency (1-10)', 'accessor': 'pro'},
          {'Header': "Job Matches",'accessor': "jobMatch"}
        ],
      }

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')


print("Starting server")

if __name__ == '__main__':
    
    if standup_db:
        print("")
        print("Creating tables and seeding dummy data")
        print("")
        db.createAndSeedTables()

    # Will set port to 5000 on local machine, but allow Heroku to bind on deployment.
    port = int(os.environ.get('PORT', 80))
    # app.run(host='0.0.0.0', port=port)
    app.run(host='0.0.0.0', port=8766) ## <-- leave this for Isaac for the time-being
