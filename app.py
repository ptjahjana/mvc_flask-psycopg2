# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
from mvc_flask import FlaskMVC

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
FlaskMVC(app)