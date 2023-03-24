# Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# initializing our app
app = Flask(__name__)
app.debug = True

# Configs
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cas@cas/dont_let_them_perish'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 

# Modules
db = SQLAlchemy(app)

# Models


# Schema Objects
# Our schema objects will go here

# Routes
# Our GraphQL route will go here

@app.route('/')
def index():
    return 'Welcome to Don\'t let them perish API'
if __name__ == '__main__':
     app.run()

