from abc import ABC, abstractmethod

import requests


class HH_API_ABC(ABC):
    """
    Абстрактный класс для HeadHunterAPI.
    """

    @abstractmethod
    def get_vacancies(self, params=None):
        pass


class HeadHunterAPI(HH_API_ABC):
    """
    Класс, наследующийся от абстрактного класса, для работы с платформой hh.ru.
    """

    def __init__(self):
        self.base_url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, params=None):
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json().get("items", [])
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при обращении к API: {e}")
            return []