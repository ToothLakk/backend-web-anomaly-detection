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
    result = dao.createUser(data['name'], data['password'], data['role'])
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

# get all user
@app.route('/get_all_user', methods=['POST'])
def getAllUser():
    data = request.get_json()
    # app.logger.error('%s', type(data['rgb']))
    result = dao.getUser()
    return result

# delete user
@app.route('/delete_user', methods=['POST'])
def deleteUser():
    data = request.get_json()
    # app.logger.error('%s', type(data['rgb']))
    result = dao.deleteUser(data['id'])
    return result

#get help by id
@app.route('/get_help_by_id', methods=['POST'])
def getHelpByID():
    data = request.get_json()
    # app.logger.error('%s', type(data['rgb']))
    result = dao.getHelpById(data['id'])
    return result

# get all help
@app.route('/get_all_help', methods=['POST'])
def getAllHelp():
    data = request.get_json()
    # app.logger.error('%s', type(data['rgb']))
    result = dao.getAllHelp()
    return result

# create camera
@app.route('/add_camera', methods=['POST'])
def addCamera():
    data = request.get_json()
    # app.logger.error('%s', type(data['rgb']))
    result = dao.addCamera( data['userid'], data['cameraname'])
    return result

#get camera by id
@app.route('/get_camera_by_id', methods=['POST'])
def getCameraByID():
    data = request.get_json()
    # app.logger.error('%s', type(data['rgb']))
    result = dao.getCameraById(data['id'])
    return result

# get camera by userID
@app.route('/get_camera_by_userID', methods=['POST'])
def getCameraByUserID():
    data = request.get_json()
    # app.logger.error('%s', type(data['rgb']))
    result = dao.getCameraByUserId(data['id'])
    return result

#update camera name
@app.route('/update_camera_name', methods=['POST'])
def updateCameraName():
    data = request.get_json()
    # app.logger.error('%s', type(data['rgb']))
    result = dao.updateCameraName(data['name'], data['id'])
    return result

# delete camera (update delete_flag = 1)
@app.route('/delete_camera', methods=['POST'])
def deleteCamera():
    data = request.get_json()
    # app.logger.error('%s', type(data['rgb']))
    result = dao.deleteCamera(data['id'])
    return result


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1000)
