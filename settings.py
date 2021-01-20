from flask_cors import CORS
from flask import Flask


app = Flask(__name__)
cors = CORS(app, allow_headers="token", expose_headers="token")

USERNAME = "fbowuamlkpivet"
PASSWORD = "84b4f0be6d54abd24d3d67d2e39d9bd0407acb5b01f18771149a0eae4f6d09ed"
HOST = "ec2-34-253-148-186.eu-west-1.compute.amazonaws.com"
PORT = 5432
DB = "d33p4j3lb9sb31"

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgres://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["TOKEN_VALIDITY_SECONDS"] = 500