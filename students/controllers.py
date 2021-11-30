from flask import Flask, jsonify

from .models import StudentsRepository


def init_controllers(app: Flask):
    @app.route("/students", methods=["GET", "POST"])
    def index():
        sr = StudentsRepository("students.json")

        return jsonify({"students": sr.get_all()})
