import os
import json
import uuid
from typing import Any, Dict, Optional


class StudentsRepository:

    def __init__(self, path: str) -> None:
        if not os.path.isfile(path):
            open(path, 'w').close()
        self.path = path

    def store(self, student: Dict[str, Any]) -> None:
        student.update({"id": str(uuid.uuid4())})

        with open(self.path, 'r+') as f:
            db = json.load(f)
            db['students'].append(student)
            f.seek(0)
            json.dump(db, f, indent=4)

    def get_all(self) -> dict:
        with open(self.path, 'r') as f:
            db = json.load(f)

        return db['students']

    def get_by_id(self, id: str) -> Optional[Dict[str, Any]]:
        with open(self.path, 'r') as f:
            db = json.load(f)

            for student in db['students']:
                if student.get('id') == id:
                    return student

            return None

    def update_by_id(self, id: str, new_student: Dict[str, Any]) -> Optional[Dict[str, Any]]:  # noqa: E501
        with open(self.path, 'r+') as f:
            db = json.load(f)

            for student in db['students']:
                if student.get('id') == id:
                    student.update(new_student)

                    f.seek(0)
                    json.dump(db, f, indent=4)

                    return student

            return None

    def delete_by_id(self, id: str) -> Optional[Dict[str, Any]]:
        with open(self.path, 'r+') as f:
            db = json.load(f)

            deleted_student = None

            for student in db['students']:
                if student.get('id') == id:
                    deleted_student = student
                    break

            if not deleted_student:
                return None

            db['students'].remove(deleted_student)

            # Save is not working when db is less than before.
            f.seek(0)
            json.dump(db, f, indent=4)

            return deleted_student
