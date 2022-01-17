from pydoc import render_doc
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template, redirect, request, jsonify
from ..models import employee

@app.route('/')
def index():
    all_employees = employee.Employee.get_all()
    return render_template('index.html', all_employees=all_employees)

@app.route('/ajax/live/search', methods=["GET", "POST"])
def ajax_live_search():
    if request.method == "POST":
        print(request.form['query'])
        data = {
        'search_word':  f"%%{request.form['query']}%%"
        }
        employees = employee.Employee.search_for_employees(data)
    return jsonify({'htmlresponse': render_template('response.html', employees = employees)})