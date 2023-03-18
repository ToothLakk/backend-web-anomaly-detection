import flask
import dao
from flask import request
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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1000)
day la mot doan code loi