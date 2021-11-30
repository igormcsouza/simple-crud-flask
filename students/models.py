import json
import os
from typing import Any, Dict


class StudentsRepository:

    def __init__(self, path: str) -> None:
        if not os.path.isfile(path):
            open(path, 'w').close()
        self.path = path

    def store(self, student: Dict[str, Any]) -> None:
        with open(self.path, 'r+') as f:
            db = json.load(f)
            db['students'].append(student)
            f.seek(0)
            json.dump(db, f, indent=4)

    def get_all(self) -> dict:
        with open(self.path, 'r') as f:
            db = json.load(f)

        return db['students']

    def get_one(self, id: str) -> None:
        ...

    def update(self, student: Dict[str, Any]) -> None:
        ...

    def delete(self, student: Dict[str, Any]) -> None:
        ...
