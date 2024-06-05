
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
from dotenv import load_dotenv
import os
from flask_migrate import Migrate

from flask_bcrypt import Bcrypt
from flask_login import LoginManager



load_dotenv()

app = Flask(__name__)

import datetime  # Import datetime module

app.config['SECRET_KEY'] = os.getenv('FLASK_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')

db = SQLAlchemy(app) #DATABASE INSTANCE
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

with app.app_context():
    db.create_all()

from firstproject import routes