from src.vacancies import Vacancies

def test_vacancies_basic():
    data = {
        "name": "Тестовая вакансия",
        "url": "http://example.com",
        "salary": {"from": 50000},
        "snippet": {
            "requirement": "Требование",
            "responsibility": "Обязанность"
        }
    }
    vac = Vacancies(data)

    assert vac.name == "Тестовая вакансия"
    assert vac.url == "http://example.com"
    assert vac.salary == 50000
    assert "Требование" in vac.description
    assert "Обязанность" in vac.description

def test_vacancies_default_values():
    vac = Vacancies({})

    assert vac.name == "Без названия"
    assert vac.url == "Ссылка отсутствует"
    assert vac.salary == "Зарплата не указана"
    assert vac.description == "Описание отсутствует"
