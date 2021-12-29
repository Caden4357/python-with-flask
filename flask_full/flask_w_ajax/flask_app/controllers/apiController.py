from flask import jsonify
from flask_app import app
@app.route('/get_data')
def get_data():
    # jsonify will serialize data into JSON format.
    return jsonify(message="Hello World")