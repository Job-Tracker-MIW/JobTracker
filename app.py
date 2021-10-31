from flask import Flask, render_template, request, jsonify, make_response
import os

import flask
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

@app.route('/images/<path:filename>')
def base_static(filename):
    return send_from_directory(app.root_path + '/images/', filename)

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
def get_companytable():

    userid = db.getUserForMock()
    val =  db.getTableCompanies(userid)
    return {"tableData": val}

@app.route('/companies', methods=['POST'])
def addCompany():
  userid = db.getUserForMock()
  company = request.get_json()
  wasAdded = db.addCompany(company, userid)

  if wasAdded:
    return flask.Response(status=201)
  else:
    return flask.Response(status=403)

@app.route('/companies/<companyid>', methods=['PUT'])
def updateCompany(companyid):
  userid = db.getUserForMock()
  company = request.get_json()
  print(company)
  wasUpdated = db.updateCompany(company, userid, int(companyid))

  if wasUpdated:
    return flask.Response(status=201)
  else:
    return flask.Response(status=403)

@app.route('/companies/<companyid>', methods=['DELETE'])
def deleteCompany(companyid):
  wasDeleted = db.deleteCompany(int(companyid))

  if wasDeleted:
    return flask.Response(status=201)
  else:
    return flask.Response(status=403)

@app.route("/skills")
def get_skilltable():

    userid = db.getUserForMock()
    val =  db.getTableSkills(userid)
    return {"tableData": val}

@app.route('/skills', methods=['POST'])
def addSkill():
  userid = db.getUserForMock()
  skill = request.get_json()
  wasAdded = db.addSkill(skill, userid)

  if wasAdded:
    return flask.Response(status=201)
  else:
    return flask.Response(status=403)

@app.route('/skills/<skillid>', methods=['PUT'])
def updateSkill(skillid):
  userid = db.getUserForMock()
  skill = request.get_json()
  print(skill)
  wasUpdated = db.updateSkill(skill, userid, int(skillid))

  if wasUpdated:
    return flask.Response(status=201)
  else:
    return flask.Response(status=403)

@app.route('/skills/<skillid>', methods=['DELETE'])
def deleteSkill(skillid):
  wasDeleted = db.deleteSkill(int(skillid))

  if wasDeleted:
    return flask.Response(status=201)
  else:
    return flask.Response(status=403)

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
