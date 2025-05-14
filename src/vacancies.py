class Vacancies:
    """
    Класс для работы с вакансиями.
    """

    def __init__(self, vac):
        self.name = vac.get("name", "Без названия")
        self.url = vac.get("url", "Ссылка отсутствует")
        self.salary = self.get_salary_from(vac.get("salary"))
        snippet = vac.get("snippet", {})
        self.description = self.format_description(snippet)

    def get_salary_from(self, salary):
        if salary and salary.get("from"):
            return salary["from"]
        else:
            return "Зарплата не указана"

    def format_description(self, snippet):
        requirement = snippet.get("requirement", "")
        responsibility = snippet.get("responsibility", "")
        desc = requirement
        if responsibility:
            desc += " " + responsibility
        return desc.strip() if desc else "Описание отсутствует"

    def to_dict(self):
        """
        Метод для преобразования объекта в словарь для записи в JSON.
        """
        return {
            "name": self.name,
            "url": self.url,
            "salary": self.salary,
            "description": self.description
        }

    @staticmethod
    def validate_salary(salary):
        if salary is None or salary <= 0:
            return "Зарплата не указана"
        return salary

    def __lt__(self, other):
        if isinstance(other, Vacancies):
            return self.salary < other.salary
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Vacancies):
            return self.salary > other.salary
        return NotImplemented

    def __str__(self):
        return f"""Название: {self.name}
    Ссылка: {self.url}
    Зарплата: {self.salary}
    Описание: {self.description}
    """