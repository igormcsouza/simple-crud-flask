from flask import jsonify, request

from students.models import StudentsRepository


repository = StudentsRepository(path="students.json")


def index():
    if request.method == 'GET':
        return jsonify({"students": repository.get_all()})

    if request.method == 'POST':
        repository.store(request.json)  # type: ignore
        return jsonify(), 201
