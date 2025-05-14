import pytest
from src.hh_api import HeadHunterAPI

def test_get_vacancies_returns_list(monkeypatch):
    class MockResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {
                "items": [{"id": "1", "name": "Test Vacancy"}]
            }

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("src.hh_api.requests.get", mock_get)

    api = HeadHunterAPI()
    result = api.get_vacancies({"text": "test"})

    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["name"] == "Test Vacancy"
