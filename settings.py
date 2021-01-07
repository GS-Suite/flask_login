from flask_cors import CORS
from flask import Flask


app = Flask(__name__)
cors = CORS(app, allow_headers="token", expose_headers="token")

USERNAME = "rrxadatmboggjn"
PASSWORD = "6bd91716dce7db5ca843eb6ec5b2754da11aa0fa6ec87d018df95ab7e136e340"
HOST = "ec2-54-170-100-209.eu-west-1.compute.amazonaws.com"
PORT = 5432
DB = "d40uo16es6lt9h"

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgres://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
