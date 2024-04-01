from flask import Flask
from flask_cors import CORS

app = Flask(__name__, template_folder='./../client/html')
CORS(app, origins=['https://626ef8539c2a85c784499fd724765f22.serveo.net'])

