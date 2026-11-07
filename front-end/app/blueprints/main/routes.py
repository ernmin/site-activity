from flask import Blueprint, render_template
from app.blueprints.main import main_bp
# app.register_blueprint(search, url_prefix="/search")

@main_bp.route('/')
def index():
    return render_template('index.html')