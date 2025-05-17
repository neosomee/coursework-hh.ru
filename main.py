from src.hh_api import HeadHunterAPI
from src.filters import filter_word
from src.vacancies import Vacancies
from src.file_reader_abc import WorkingWithData


def main() -> None:
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий (через пробел): ").split()

    hh_api = HeadHunterAPI()
    data_handler = WorkingWithData(filepath="data/data.json")

    vacancies_data = hh_api.get_vacancies({"text": search_query, "per_page": top_n})

    if isinstance(vacancies_data, dict):
        vacancies_list = vacancies_data.get("items", [])
    else:
        vacancies_list = vacancies_data

    vacancy_objects = []

    for vacancy in vacancies_list:
        vacancy_obj = Vacancies(vacancy)
        vacancy_objects.append(vacancy_obj)
        data_handler.save_vacancy(vacancy_obj.to_dict())

    saved_vacancies = data_handler.read_vacancy()
    print("Сохраненные вакансии из файла:")
    for vac in saved_vacancies:
        print(vac)
        print("-" * 40)

    print("\nВакансии, полученные с API:")
    for vac_obj in vacancy_objects:
        print(vac_obj)
        print("-" * 40)

    filtered_vacancies = filter_word({"items": vacancies_list}, filter_words)
    print("\nОтфильтрованные вакансии:")
    for vac in filtered_vacancies:
        vacancy_obj = Vacancies(vac)
        print(vacancy_obj)
        print("-" * 40)


if __name__ == "__main__":
    main()
