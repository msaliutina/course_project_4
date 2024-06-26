import os
from src.vacancy import Vacancy
from src.vac_loader_hh import HHLoader
from src.vac_filtering import get_salary_range, filter_vacancies_by_prompt, filter_vacancies_by_salary, sort_by_salary_upper_limit
from src.vac_storage_json import JSONVacanciesStorage

# Функция для взаимодействия с пользователем
def user_interaction():
    '''
    Функция для взаимодействия с пользователем по работе с вакансиями.
    Пользователь вводит параметры поиска вакансий (название, зарплата, ключевые слова),
    загружает вакансии с помощью HH API, фильтрует и сортирует их, затем сохраняет
    отфильтрованные и отсортированные данные в JSON файл'''
    hh_api = HHLoader()
    type_of_vacancy = input("Введите интересующее название вакансии: ")
    hh_vacancies = hh_api.load_vacancies(type_of_vacancy)
    vacancies_list_ed = []
    for vacancy in hh_vacancies:
        vacancy_dict = vacancy.to_dict()
        vacancies_list_ed.append(Vacancy.from_dict(vacancy_dict))
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    salary_range_lower = get_salary_range("Введите нижние границы зарплат (одно или два числа через запятую): ")
    salary_range_upper = get_salary_range("Введите верхние границы зарплат (одно или два числа через запятую): ")
    prompt = input("Введите ключевые слова для фильтрации вакансий: ")
    salary_currency = input("Введите желаемую валюту зарплаты: ")
    filtered_vacancies = filter_vacancies_by_prompt(vacancies_list_ed, prompt)
    ranged_vacancies = filter_vacancies_by_salary(filtered_vacancies, salary_range_lower, salary_range_upper, salary_currency)
    sorted_vacancies = sort_by_salary_upper_limit(ranged_vacancies)
    if top_n <= len(sorted_vacancies):
        top_vacancies = sorted_vacancies[:top_n]
    else:
        top_vacancies = sorted_vacancies
    file_path_2 = os.path.join(os.getcwd(), 'data', 'selected_vacancies.json')
    os.makedirs(os.path.dirname(file_path_2), exist_ok=True)
    open(file_path_2, 'a').close()
    json_storage = JSONVacanciesStorage(file_path_2)
    json_storage.add_vacancy(top_vacancies)
    json_storage.get_all_vacancies()
    print('Список вакансий находится в файле selected_vacancies.json в папке data')
    clean_file = input("Хотите стереть список вакансий в файле (да/нет)? ").lower()
    if clean_file == 'да':
        json_storage.clear()

if __name__ == "__main__":
    user_interaction()