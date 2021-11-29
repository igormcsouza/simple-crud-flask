from typing import Any, Dict, List
from flask import Flask, jsonify, request


app = Flask(__name__)


students: List[Dict[str, Any]] = []


@app.route("/students", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        students.append(request.json)  # type: ignore

        return jsonify(), 201

    return jsonify({"students": students})


@app.route("/students/<int:id>", methods=["GET", "PUT", "DELETE"])
def get_one_record(id: int):
    try:
        student = students[id]
    except IndexError:
        return jsonify({"details": "Student not found"}), 404

    if request.method == "GET":
        return jsonify({"student": student})

    if request.method == "PUT":
        student.update(request.json)  # type: ignore
        return jsonify(), 204

    if request.method == "DELETE":
        students.remove(student)
        return jsonify(), 204
