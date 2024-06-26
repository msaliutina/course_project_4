import ast
from src.vacancy import Vacancy


def filter_vacancies_by_prompt(vacancies: list[Vacancy], prompt: str) -> list[Vacancy]:
    '''Фильтрует список вакансий по ключевым словам из запроса. Возвращает тфильтрованный список объектов вакансий'''
    vacancies_filtered = []
    for vac in vacancies:
        str_to_find_in = f'{vac.title}; {vac.place}; {vac.requirement}; {vac.responsibility}'.lower()
        words = [word for word in prompt.lower().split() if word]
        if all(word in str_to_find_in for word in words):
            vacancies_filtered.append(vac)
    return vacancies_filtered

def get_salary_range(prompt):
    '''Получает диапазон зарплат из пользовательского ввода'''
    user_input = input(prompt)
    if user_input.strip():  # Проверка на непустой ввод
        try:
            user_input = user_input.strip()
            if ',' not in user_input:
                # Если введено одно число, используем его как нижний или верхний предел
                value = int(user_input)
                return (value, None)  # Нижний предел
            else:
                return ast.literal_eval(user_input)
        except (SyntaxError, ValueError):
            print("Некорректный ввод. Используйте формат (min, max) или одно число.")
            return get_salary_range(prompt)
    else:
        return None, None
def filter_vacancies_by_salary(vacancies: list[Vacancy],
                               salary_lower_limit_range: tuple[int | None, int | None] = None,
                               salary_upper_limit_range: tuple[int | None, int | None] = None,
                               salary_currency: str = None) -> list[Vacancy]:
    '''Фильтрует список вакансий по заданным условиям зарплаты и валюте'''
    if salary_currency is not None:
        vacancies = [item for item in vacancies if salary_currency == item.salary_currency]

    lower_min, lower_max = salary_lower_limit_range
    upper_min, upper_max = salary_upper_limit_range

    if lower_min is not None or lower_max is not None:
        if lower_min is not None and lower_max is not None:
            vacancies = [item for item in vacancies if lower_min <= item.salary_lower_limit <= lower_max]
        else:
            vacancies = [item for item in vacancies if
                         (lower_min is None or item.salary_lower_limit >= lower_min) and
                         (lower_max is None or item.salary_lower_limit >= lower_max)]

    if upper_min is not None or upper_max is not None:
        if upper_min is not None and upper_max is not None:
            vacancies = [item for item in vacancies if upper_min <= item.salary_upper_limit <= upper_max]
        else:
            vacancies = [item for item in vacancies if
                         (upper_min is None or item.salary_upper_limit <= upper_min) and
                         (upper_max is None or item.salary_upper_limit <= upper_max)]

    return vacancies


def sort_by_salary_upper_limit(vacancies: list[Vacancy]) -> list[Vacancy]:
    '''Сортирует список вакансий по верхней границе зарплаты в порядке убывания'''
    return sorted(vacancies, key=lambda x: x.salary_upper_limit, reverse=True)
