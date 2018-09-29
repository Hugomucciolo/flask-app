from flask import Flask, render_template, flash, redirect, request, jsonify
from config import db
from Blueprints.users import users

app = Flask(__name__)
app.register_blueprint(users)
app.secret_key = 'flask-app'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/docker')
def docker():
    return render_template('docker.html')

@app.route('/jenkins')
def jenkins():
    return render_template('jenkins.html')

app.run(host='0.0.0.0',port=80, debug=True)

# import os
# from flask import Flask, jsonify, make_response

# app = Flask(__name__)

# @app.route('/')
# def index():
#     nome = os.environ['APP_NOME'] if 'APP_NOME' in os.environ else 'Default'
#     return jsonify({'message' : 'Running!', 'app' : nome})

# @app.route('gitlab')
# def index():
#     return jsonify({'message' : 'oi, estou no gitlab'})

# app.run(host='0.0.0.0',port=80)
