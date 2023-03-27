# Imports
from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_graphql import GraphQLView
import os

from db import db

from src.graphql.schema import schema
from src.views.rooms import bp as rooms_bp
from src.views.plants import bp as plants_bp

# initializing app
app = Flask(__name__)
app.debug = True
load_dotenv()
database_url = os.getenv('DATABASE_URL')

# Configs
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 

# initialize the SQLAlchemy object with the Flask app
db.init_app(app)

# Modules
migrate = Migrate(app, db)

# Routes
app.add_url_rule(
    '/graphql-api',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)


app.register_blueprint(rooms_bp)
app.register_blueprint(plants_bp)

@app.route('/')
def index():
  return 'Welcome to Don\'t let them perish API'

if __name__ == '__main__':
     app.run()

