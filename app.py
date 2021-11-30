from flask import Flask

import students


app = Flask(__name__)

# Initialize the apps
students.init_app(app)
