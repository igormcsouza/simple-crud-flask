import json
from typing import Any, Dict


class StudentsRepository:

    def __init__(self, path: str) -> None:
        self.path = path

    def store(self, student: Dict[str, Any]) -> None:
        with open(self.path, 'rb') as f:
            db = json.load(f)

        db.append(student)

        with open(self.path, 'wb') as f:
            json.dump(f, db)

    def get_all(self) -> dict:
        with open(self.path, 'rb') as f:
            db = json.load(f)

        return db['students']
