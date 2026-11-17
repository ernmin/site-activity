from flask import Blueprint

# 1. Create the blueprint instance
search_bp = Blueprint('search', __name__)

# 2. Import routes at the bottom to register them and avoid circular imports
from app.blueprints.search import routes