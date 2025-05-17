import json
import pytest
from src.file_reader_abc import WorkingWithData

def test_save_and_read(tmp_path):
    file = tmp_path / "data.json"
    file.parent.mkdir(parents=True, exist_ok=True)

    if not file.exists():
        file.write_text("[]", encoding="utf-8")

    handler = WorkingWithData(str(file))

    assert handler.read_vacancy() == []

    vacancy = {"id": "1", "name": "Test"}
    handler.save_vacancy(vacancy)

    data = handler.read_vacancy()
    assert len(data) == 1
    assert data[0]["id"] == "1"


def test_delete_vacancy(tmp_path):
    file = tmp_path / "data.json"
    vacancies = [
        {"id": "1", "name": "Vac1"},
        {"id": "2", "name": "Vac2"},
    ]
    file.write_text(json.dumps(vacancies), encoding="utf-8")

    handler = WorkingWithData(str(file))
    handler.delete_vacancy("1")

    data = handler.read_vacancy()
    assert len(data) == 1
    assert data[0]["id"] == "2"
