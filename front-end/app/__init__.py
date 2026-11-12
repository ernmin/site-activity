from flask import Flask
# from app.extensions import db, migrate
# from app.config import Config

def create_app():
    app = Flask(__name__)
    

    # Initialize Flask extensions
    # db.init_app(app)
    # migrate.init_app(app, db)

    # Register Blueprints
    from app.blueprints.main import main_bp
    app.register_blueprint(main_bp)

    from app.blueprints.search import search_bp
    app.register_blueprint(search_bp)
    # from app.blueprints.auth import auth_bp
    # app.register_blueprint(auth_bp, url_prefix='/auth')

    return app