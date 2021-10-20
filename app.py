from flask import Flask, render_template, request, jsonify, make_response
import os
import database.database_config as db
from dotenv import load_dotenv
from flask.helpers import send_file

load_dotenv()

app = Flask(__name__, static_folder="client/build/static", template_folder="client/build")

@app.route('/')
def root():
    return render_template('index.html')

@app.route("/welcome_msg")
def get_current_msg():
        return {"msg": "Welcome folks"}


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

@app.route("/table")
def get_table():
    return {"tableData": [
                           { 'col1': 'Hello', 'col2': 'World',},
                           { 'col1': 'react-table', 'col2': 'rocks',},
                           { 'col1': 'whatever', 'col2': 'you want',},
                         ]
                         }


            #{ 
            #               'col1': ['Hello', 'react-table', 'whatever'],
            #               'col2': ['World', 'rocks', 'you want']
            #               }}



print("Starting server")

if __name__ == '__main__':
    
    if os.environ["DB_CREATE_SEED"] == "True" or os.environ["DB_CREATE_SEED"] == "true":
        print("")
        print("Creating tables and seeing dummy data")
        print("")
        db.createAndSeedTables()

    # Will set port to 5000 on local machine, but allow Heroku to bind on deployment.
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)
