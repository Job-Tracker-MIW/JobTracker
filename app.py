import datetime
from flask import Flask, render_template, request, jsonify, make_response
import os
import jwt
import flask
import database.database_config as db
from dotenv import load_dotenv
from flask.helpers import send_file
from flask import send_from_directory 
from functools import wraps

# flag for standing up database locally
standup_db = False

load_dotenv()

app = Flask(__name__, static_folder="client/build/static", template_folder="client/build")
app.config['SECRET_KEY'] = 'secretkey'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('token')

        if not token:
            return render_template('index.html')
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return render_template('index.html')

        return f(*args, **kwargs)
    
    return decorated

# basic routes

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

# appjobs endpoints

@app.route("/appjobs")
@token_required
def get_jobtable():

    userid = jwt.decode(request.headers.get('token'), app.config['SECRET_KEY'])['userid']
    val =  db.getTableApplications(userid)

    return {"tableData": 
        val,
            "tableColumns":  [
        {'Header': 'Title', 'accessor': 'title'},
        {'Header': 'Company', 'accessor': "company"},
        {'Header': "Application Date",'accessor': "appdt"}
        ],
      }

# contacts endpoints

@app.route("/contacts", methods=["GET"])
@token_required
def get_conttable():
    userid = jwt.decode(request.headers.get('token'), app.config['SECRET_KEY'])['userid']
    val =  db.getTableContacts(userid)
    print(val)

    return {"tableData": val } #,
      #"tableColumns":  [
      #  {'Header': 'Contact', 'accessor': 'contact'},
      #  {'Header': 'E-Mail', 'accessor': 'email'},
      #  {'Header': 'Phone', 'accessor': 'phone'},
      #  {'Header': 'Companies', 'accessor': "company"},
      #  {'Header': "Job Matches",'accessor': "jobCount"}
      #  ],
      #}


@app.route('/contacts', methods=['POST'])
@token_required
def addContact():
  userid = jwt.decode(request.headers.get('token'), app.config['SECRET_KEY'])['userid']
  contact = request.get_json()

  print('here --->', contact)
  wasAdded = db.addContact(contact, userid)

  if wasAdded:
    return flask.Response(status=201)
  else:
    return flask.Response(status=403)

@app.route('/contacts/<contactid>', methods=['PUT'])
@token_required
def updateContact(contactid):
  userid = jwt.decode(request.headers.get('token'), app.config['SECRET_KEY'])['userid']
  contact = request.get_json()

  wasUpdated = db.updateContact(contact, userid, int(contactid))

  if wasUpdated:
    return flask.Response(status=201)
  else:
    return flask.Response(status=403)

@app.route('/contacts/<contactid>', methods=['DELETE'])
@token_required
def deleteContact(contactid):
  print('toDeleted')
  userid = jwt.decode(request.headers.get('token'), app.config['SECRET_KEY'])['userid']

  wasDeleted = db.deleteContact(int(contactid))

  print('wasDeleted', wasDeleted)

  if wasDeleted:
    return flask.Response(status=201)
  else:
    return flask.Response(status=403)




# companies endpoints

@app.route("/companies")
@token_required
def get_comptable():
    userid = jwt.decode(request.headers.get('token'), app.config['SECRET_KEY'])['userid']
    val =  db.getTableCompanies(userid)
    return {"tableData": val, 
      "tableColumns":  [
          {'Header': 'Company', 'accessor': "company"},
          {'Header': 'Contacts', 'accessor': 'contact'},
          {'Header': "Job Matches",'accessor': "jobCount"}
        ],
      }

# skills endpoints

@app.route("/skills", methods=["GET"])
@token_required
def get_skilltable():
    userid = jwt.decode(request.headers.get('token'), app.config['SECRET_KEY'])['userid']
    print(userid)
    val =  db.getTableSkills(userid)
    return {"tableData": val}

@app.route('/skills', methods=['POST'])
@token_required
def addSkill():
  userid = jwt.decode(request.headers.get('token'), app.config['SECRET_KEY'])['userid']
  skill = request.get_json()
  wasAdded = db.addSkill(skill, userid)

  if wasAdded:
    return flask.Response(status=201)
  else:
    return flask.Response(status=403)

@app.route('/skills/<skillid>', methods=['PUT'])
@token_required
def updateSkill(skillid):
  userid = jwt.decode(request.headers.get('token'), app.config['SECRET_KEY'])['userid']
  skill = request.get_json()
  print(skill)
  wasUpdated = db.updateSkill(skill, userid, int(skillid))

  if wasUpdated:
    return flask.Response(status=201)
  else:
    return flask.Response(status=403)

@app.route('/skills/<skillid>', methods=['DELETE'])
@token_required
def deleteSkill(skillid):
  userid = jwt.decode(request.headers.get('token'), app.config['SECRET_KEY'])['userid']
  wasDeleted = db.deleteSkill(int(skillid))

  if wasDeleted:
    return flask.Response(status=201)
  else:
    return flask.Response(status=403)

# authentication endpoints

@app.route('/login', methods=['POST'])
def checklogin():
    sent_info = request.get_json()
    userid = db.check_login(sent_info)
    if userid is not None:
        token = jwt.encode({'userid': userid, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)}, app.config['SECRET_KEY'])
        return jsonify({'response': True, 'token': token.decode('UTF-8')})
    return jsonify({'response': False})

# no endpoint found
@app.errorhandler(404)
def not_found(e):
    return render_template('index.html')


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
