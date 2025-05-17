from abc import ABC, abstractmethod
import json


class Reader_ABC(ABC):
    @abstractmethod
    def save_vacancy(self, data_to_add):
        """
        Абстрактный метод для сохранения вакансии.
        """
        pass

    @abstractmethod
    def read_vacancy(self):
        """
        Абстрактный метод для чтения вакансий из файла.
        """
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id):
        """
        Абстрактный метод для удаления вакансии по идентификатору.
        """
        pass


class WorkingWithData(Reader_ABC):
    def __init__(self, filepath: str):
        """
        Инициализация с указанием пути к файлу.
        """
        self.__filepath: str = filepath

    def read_vacancy(self):
        """
        Чтение списка вакансий из JSON-файла.
        """
        try:
            with open(self.__filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data if isinstance(data, list) else []
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_vacancy(self, data_to_add):
        """
        Добавление вакансии в файл без дублирования.
        """
        existing_data = self.read_vacancy()

        if not any(item.get("url") == data_to_add.get("url") for item in existing_data):
            existing_data.append(data_to_add)

            with open(self.__filepath, "w", encoding="utf-8") as file:
                json.dump(existing_data, file, indent=4, ensure_ascii=False)

    def delete_vacancy(self, vacancy_id):
        """
        Удаление вакансии по идентификатору из файла.
        """
        new_data = self.read_vacancy()
        new_data = [data for data in new_data if data.get("id") != vacancy_id]

        with open(self.__filepath, "w", encoding="utf-8") as file:
            json.dump(new_data, file, indent=4, ensure_ascii=False)
