# Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

from models import Room


# initializing our app
app = Flask(__name__)
app.debug = True
load_dotenv()
database_url = os.getenv('DATABASE_URL')


# Configs
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 

# Modules
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Models

    
# Schema Objects
# Our schema objects will go here

# Routes
# Our GraphQL route will go here

@app.route('/')
def index():
    # db.create_all()
    # kitchen = Room(name='Kitchen', plant_count=2)
    # db.session.add(kitchen)
    # db.session.commit()
    return 'Welcome to Don\'t let them perish API'
if __name__ == '__main__':
     app.run()

