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
    data = {
        'search_word':  f"%%{request.form['query']}%%"
        }
    if request.method == "POST":
        if data['search_word'] == '':
            employees = employee.Employee.get_in_order_by_id()
        else:
            employees = employee.Employee.search_for_employees(data)
    return jsonify({'htmlresponse': render_template('response.html', employees = employees)})