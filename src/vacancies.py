class Vacancies:
    __slots__ = ("name", "url", "salary", "description")

    def __init__(self, vac):
        """
        Инициализация вакансии из словаря.
        """
        self.name: str = vac.get("name", "Без названия")
        self.url: str = vac.get("url", "Ссылка отсутствует")
        self.salary = self.__validate_salary(self.get_salary_from(vac.get("salary")))
        snippet = vac.get("snippet", {})
        self.description: str = self.format_description(snippet)

    def get_salary_from(self, salary):
        """
        Получение значения зарплаты из словаря salary.
        """
        if salary and salary.get("from"):
            return salary["from"]
        else:
            return "Зарплата не указана"

    def format_description(self, snippet):
        """
        Форматирование описания вакансии из snippet.
        """
        requirement = snippet.get("requirement", "")
        responsibility = snippet.get("responsibility", "")
        desc = requirement
        if responsibility:
            desc += " " + responsibility
        return desc.strip() if desc else "Описание отсутствует"

    def to_dict(self):
        """
        Преобразование объекта вакансии в словарь для сохранения.
        """
        return {
            "name": self.name,
            "url": self.url,
            "salary": self.salary,
            "description": self.description
        }

    def __validate_salary(self, salary):
        """
        Приватный метод валидации зарплаты.
        """
        if salary is None or (isinstance(salary, (int, float)) and salary <= 0):
            return "Зарплата не указана"
        return salary

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Vacancies):
            return self.salary < other.salary
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Vacancies):
            return self.salary > other.salary
        return NotImplemented

    def __str__(self) -> str:
        return (
            f"Название: {self.name}\n"
            f"Ссылка: {self.url}\n"
            f"Зарплата: {self.salary}\n"
            f"Описание: {self.description}\n"
        )