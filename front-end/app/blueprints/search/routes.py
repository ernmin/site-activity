# app/blueprints/dashboard/routes.py
from flask import render_template
from app.blueprints.search import search_bp

@search_bp.route('/date')
def date():
    return render_template('search/date.html')