from flask import jsonify, request

from students.models import StudentsRepository


repository = StudentsRepository(path="students.json")


def index():
    if request.method == 'GET':
        return jsonify({"students": repository.get_all()})

    if request.method == 'POST':
        # validate json
        repository.store(request.json)  # type: ignore
        return jsonify(), 201


def manage_single_student(id: str):
    if request.method == 'GET':
        student = repository.get_by_id(id)

        if not student:
            return jsonify({"detail": "Id not found on Student database."}), 404  # noqa: E501

        return jsonify(student), 200

    if request.method == 'PUT':
        student = repository.update_by_id(id, request.json or {})

        if not student:
            return jsonify({"detail": "Id not found on Student database."}), 404  # noqa: E501

        return jsonify(), 204

    if request.method == 'DELETE':
        student = repository.delete_by_id(id)

        if not student:
            return jsonify({"detail": "Id not found on Student database."}), 404  # noqa: E501

        return jsonify(), 204
