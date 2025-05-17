from abc import ABC, abstractmethod

import requests


class HH_API_ABC(ABC):
    """
    Абстрактный класс для работы с API HeadHunter.
    """

    @abstractmethod
    def _connect(self, params=None):
        """
        Протектед абстрактный метод подключения к API.
        """
        pass

    @abstractmethod
    def get_vacancies(self, params=None):
        """
        Абстрактный метод получения вакансий.
        """
        pass


class HeadHunterAPI(HH_API_ABC):
    def __init__(self):
        self.__base_url = "https://api.hh.ru/vacancies"

    def _connect(self, params=None):
        """
        Протектед метод подключения к API HH.
        Отправляет GET-запрос с параметрами и возвращает JSON-ответ.
        """
        try:
            response = requests.get(self.__base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при обращении к API: {e}")
            return {}

    def get_vacancies(self, params=None):
        """
        Получение списка вакансий по параметрам.
        """
        data = self._connect(params)
        return data.get("items", [])