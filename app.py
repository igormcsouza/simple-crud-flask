from flask import Flask

from students.controllers import init_controllers


app = Flask(__name__)

init_controllers(app)
