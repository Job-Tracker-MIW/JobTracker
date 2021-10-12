from flask import Flask, render_template, request, jsonify, make_response
import os

from flask.helpers import send_file

app = Flask(__name__, static_folder="client/build/static", template_folder="client/build")

@app.route('/')
def root():
    return render_template('index.html')

print("Starting server")

if __name__ == '__main__':
    # Will set port to 5000 on local machine, but allow Heroku to bind on deployment.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)