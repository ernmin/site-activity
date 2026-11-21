from flask import Flask
from .load_json import init_db

def create_app():
    app = Flask(__name__)

    init_db()

    #register blueprints
    from app.blueprints.main import main_bp
    app.register_blueprint(main_bp)

    return app