from flask import Blueprint

main_bp = Blueprint('main', __name__)

# Imported at the bottom so the blueprint object exists 
# before the routes try to attach to it
# from app.blueprints.main import routes