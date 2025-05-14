class Vacancies:
    """
    Класс для работы с вакансиями.
    """

    def __init__(self, vac):
        self.name = vac["name"]
        self.url = vac["url"]
        self.salary = vac["salary"]["from"] if vac["salary"] else 0

    def to_dict(self):
        """
        Метод для преобразования объекта в словарь для записи в JSON.
        """
        return {"name": self.name, "url": self.url, "salary": self.salary}

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

    def __repr__(self):
        return f"Vacancy(name='{self.name}', url='{self.url}', salary='{self.salary}')"