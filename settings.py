from flask_cors import CORS
from flask import Flask


app = Flask(__name__)
cors = CORS(app, allow_headers="token", expose_headers="token")

USERNAME = "gdcrufqvtvrjrh"
PASSWORD = "1a57336a9436b8167b1df846b8f9f576c1389eb17431d07d3caccda15fa196c4"
HOST = "ec2-34-251-118-151.eu-west-1.compute.amazonaws.com"
PORT = 5432
DB = "db0o9o3gl2l3l0"

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgres://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
