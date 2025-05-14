from src.hh_api import HeadHunterAPI
from src.vacancies import Vacancies
from src.file_reader_abc import WorkingWithData


def user_interaction() -> None:
    hh_api = HeadHunterAPI()

    search_query = input("Введите поисковый запрос для вакансий: ")

    vacancies_data = hh_api.get_vacancies({"text": search_query})

    vacancy_objects = []

    for vacancy in vacancies_data:
        vacancy_obj = Vacancies(vacancy)
        vacancy_objects.append(vacancy_obj.to_dict())

    data_handler = WorkingWithData()

    for vacancy in vacancy_objects:
        data_handler.save_vacancy(vacancy)

    saved_vacancies = data_handler.read_vacancy()
    print("Сохраненные вакансии:", saved_vacancies)


if __name__ == "__main__":
    user_interaction()