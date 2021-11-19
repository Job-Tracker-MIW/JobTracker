import datetime
from datetime import date
from flask import Flask, render_template, request, jsonify, make_response, flash
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

@app.route('/flash/<message>')
def flash(message):
  return render_template('flash.html', msg=message)

# appjobs endpoints

@app.route("/appjobs")
@token_required
def get_jobtable():

    userid = jwt.decode(request.headers.get('token'), app.config['SECRET_KEY'])['userid']
    val =  db.getTableApplications(userid)

    print('appget', val)
    return {"tableData": 
        val}

# @app.route('/appjobs', methods=['POST'])
# @token_required
# def addAppJob():
#   userid = jwt.decode(request.headers.get('token'), app.config['SECRET_KEY'])['userid']
#   application = request.get_json()

#   wasAdded = db.addApplications(application, userid)

#   if wasAdded:
#     return flask.Response(status=201)
#   else:
#     return flask.Response(status=403)

@app.route('/appjobs/<appid>', methods=['PUT'])
@token_required
def updateAppJob(appid):

  print('updating ---------------------------------------')

  userid = jwt.decode(request.headers.get('token'), app.config['SECRET_KEY'])['userid']
  application = request.get_json()

  wasUpdated = db.updateApplications(application, userid, int(appid))

  if wasUpdated:
    return flask.Response(status=201)
  else:
    return flask.Response(status=403)

@app.route('/appjobs/<appid>', methods=['DELETE'])
@token_required
def deleteAppJob(appid):


  userid = jwt.decode(request.headers.get('token'), app.config['SECRET_KEY'])['userid']

  wasDeleted = db.deleteApplications(int(appid))

  if wasDeleted:
    return flask.Response(status=201)
  else:
    return flask.Response(status=403)



@app.route('/appjobs', methods=['POST'])
@token_required
def addToApplied():
    userid = jwt.decode(request.headers.get('token'), app.config['SECRET_KEY'])['userid']
    applied_attributes = request.get_json()

    today = date.today()
    curr_datetime = today.strftime("%m/%d/%y")

    print("Applied Attributes", applied_attributes, "DATETIME", curr_datetime)

    wasAdded = db.addToApplied(userid, applied_attributes, curr_datetime)

    if wasAdded:
        return flask.Response(status=201)
    else:
        return flask.Response(status=403)


# contacts endpoints

@app.route("/contacts", methods=["GET"])
@token_required
def get_conttable():
    userid = jwt.decode(request.headers.get('token'), app.config['SECRET_KEY'])['userid']
    val =  db.getTableContacts(userid)

    return {"tableData": val }


@app.route('/contacts', methods=['POST'])
@token_required
def addContact():
  userid = jwt.decode(request.headers.get('token'), app.config['SECRET_KEY'])['userid']
  contact = request.get_json()

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

@app.route("/companies", methods=["GET", "POST", "DELETE"])
@token_required
def get_comptable():
    if request.method == 'GET':
        userid = jwt.decode(request.headers.get('token'), app.config['SECRET_KEY'])['userid']
        val =  db.getTableCompanies(userid)

        return {"tableData": val}
    
    if request.method =='POST':

        userid = jwt.decode(request.headers.get('token'), app.config['SECRET_KEY'])['userid']
        company_attributes = request.get_json()
        print("here 2", company_attributes)
        wasAdded = db.addCompany(company_attributes, userid)

        if wasAdded:
            print("Added Successfully")
            # flash("Added Successfully!")
            return flask.Response(status=201)
        else:
            # flash("Add NOT Successful")
            return flask.Response(status=403)    
    
    if request.method =='DELETE':
        userid = jwt.decode(request.headers.get('token'), app.config['SECRET_KEY'])['userid']
        company_attributes = request.get_json()
        wasDeleted = db.deleteCompany(company_attributes, userid)

        if wasDeleted:
            # flash("Delete Successful!")
            return flask.Response(status=201)
        else:
            # flash("Delete NOT Successful")
            return flask.Response(status=403)
    else:
        print("Something Went Wrong")
   

# skills endpoints

@app.route("/skills", methods=["GET"])
@token_required
def get_skilltable():
    userid = jwt.decode(request.headers.get('token'), app.config['SECRET_KEY'])['userid']
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
  wasUpdated = db.updateSkill(skill, userid, int(skillid))

  if wasUpdated:
    return flask.Response(status=201)
  else:
    return flask.Response(status=403)

@app.route('/skills/<skillid>', methods=['DELETE'])
@token_required
def deleteSkill(skillid):
  print("hello")
  userid = jwt.decode(request.headers.get('token'), app.config['SECRET_KEY'])['userid']
  wasDeleted = db.deleteSkill(int(skillid))

  if wasDeleted:
    print("Deleted skill with id " + skillid)
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

@app.route('/usersignup', methods=['POST'])
def user_signup():
  sent_info = request.get_json()
  signupSuccess = db.signup_user(sent_info)
  if signupSuccess:
    return jsonify({'response': True})
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
    app.run(host='0.0.0.0', port=8767) ## <-- leave this for Isaac for the time-being
