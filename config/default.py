"""Default configuration for the Message Board app."""
import os

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
DEBUG = False

# Example database URI (not used by the current in-memory demo)
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///' + os.path.join(BASE_DIR, 'data.db'))

# Other app-specific defaults
POSTS_PER_PAGE = 20
