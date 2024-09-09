from flask import Flask
from flask_cors import CORS

app = Flask(__name__, template_folder='./../client/html')
app.config['DEBUG'] = True
CORS(app, origins=['http://localhost:8000'])

