# app/blueprints/dashboard/routes.py
from flask import render_template, request, jsonify
from app.blueprints.search import search_bp

@search_bp.route('/date')
def date():
    return render_template('search/date.html')

@search_bp.route('/searchdate', methods=['POST'])
def searchdate():
    site_data = request.get_json()
    dateFrom = site_data.get('searchFrom', '')
    dateTo = site_data.get('searchTo', '')
    breakpoint()
    # send data to server.py at this point
    return jsonify(result=f"{dateFrom} {dateTo}")