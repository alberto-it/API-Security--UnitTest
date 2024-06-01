from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import os
from flask_migrate import Migrate

class Base(DeclarativeBase): pass

MIGRATIONS_FOLDER = os.environ.get('MIGRATIONS_FOLDER') or 'migrations'

db = SQLAlchemy(model_class=Base)
migrate = Migrate(directory=MIGRATIONS_FOLDER)