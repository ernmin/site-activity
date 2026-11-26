# app/blueprints/dashboard/routes.py
from flask import render_template, request, jsonify
from app.blueprints.search import search_bp
from app.blueprints.search.get_data import get_data

@search_bp.route('/date')
def date():
    return render_template('search/date.html')

@search_bp.route('/key')
def key():
    return render_template('search/key.html')

@search_bp.route('/searchdate', methods=['POST'])
def searchdate():
    site_data = request.get_json()
    dateFrom = site_data.get('searchFrom', '')
    dateTo = site_data.get('searchTo', '')
    table = get_data(site_data, 'searchdate')
    return table
    # send data to server.py at this point
    # return jsonify(result=f"{dateFrom} {dateTo}")


@search_bp.route('/searchkey', methods=['POST'])
def searchkey():
    site_data = request.get_json()
    siteID = site_data.get('siteID', '')
    table = get_data(site_data, 'searchkey')
    return table