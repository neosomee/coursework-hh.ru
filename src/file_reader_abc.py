from abc import ABC, abstractmethod
import json


class Reader_ABC(ABC):

    @abstractmethod
    def save_vacancy(self, data_to_add):
        pass

    @abstractmethod
    def read_vacancy(self):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id):
        pass

class WorkingWithData(Reader_ABC):
    """
    Класс для работы с файлами.
    """

    def __init__(self):
        self.filepath = "data/data.json"

    def read_vacancy(self):
        """
        Метод для чтения файла.
        """
        with open(self.filepath, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                return data if isinstance(data, list) else []
            except json.JSONDecodeError:
                return []

    def save_vacancy(self, data_to_add):
        """
        Метод для добавления информации в файл.
        """
        existing_data = self.read_vacancy()

        if isinstance(data_to_add, dict):
            existing_data.append(data_to_add)

        with open(self.filepath, "w", encoding="utf-8") as file:
            json.dump(existing_data, file, indent=4, ensure_ascii=False)

    def delete_vacancy(self, vacancy_id):
        """
        Метод для удаления данных из файла и перезаписи.
        """
        new_data = self.read_vacancy()
        new_data = [data for data in new_data if data["id"] != vacancy_id]

        with open(self.filepath, "w", encoding="utf-8") as file:
            json.dump(new_data, file, indent=4, ensure_ascii=False)