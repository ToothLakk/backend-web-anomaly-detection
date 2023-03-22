import flask
from dao import dao
from model import model
from flask import request, json
import logging
app = flask.Flask(__name__)
app.config["DEBUG"] = True
# Create some test data for our catalog in the form of a list of dictionaries.

@app.route('/', methods=['POST', 'GET'])
def home():
    return '''<h1>Anomaly detection</h1>
                <p>A API for interact with MySQL server</p>'''

@app.route('/selectTable1', methods=['POST'])
def api_id():
    data = request.get_json()
    # app.logger.error('%s', type(data['rgb']))
    result = dao.get_dta_by_id(data['id'])
    return result

@app.route('/insertTable1', methods=['POST'])
def insertTable1():
    data = request.get_json()
    # app.logger.error('%s', type(data['rgb']))
    result = dao.innsert_to_tb1(data['name'], data['age'])
    return result

# get user by id
@app.route('/get_user_by_id', methods=['POST'])
def getUserByID():
    data = request.get_json()
    # app.logger.error('%s', type(data['rgb']))
    result = dao.getUserById(data['id'])
    return result

# get user by name
@app.route('/get_user_by_name', methods=['POST'])
def getUserByName():
    data = request.get_json()
    # app.logger.error('%s', type(data['rgb']))
    result = dao.getUserByUsername(data['name'])
    return result

#create new user
@app.route('/create_user', methods=['POST'])
def createUser():
    data = request.get_json()
    # app.logger.error('%s', type(data['rgb']))
    result = dao.createUser(data['id'] ,data['name'], data['password'], data['role'])
    return result

# update user name
@app.route('/update_user_name', methods=['POST'])
def updateUserName():
    data = request.get_json()
    # app.logger.error('%s', type(data['rgb']))
    result = dao.updateUsername( data['name'], data['id'])
    return result

#update user password
@app.route('/update_user_password', methods=['POST'])
def updateUserPassword():
    data = request.get_json()
    # app.logger.error('%s', type(data['rgb']))
    result = dao.updateUserPassword( data['password'], data['id'])
    return result


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1000)
