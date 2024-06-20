import requests

from src.vacancy import Vacancy
from src.vac_loader import VacanciesLoader


class HHLoader(VacanciesLoader):
    '''Класс для загрузки вакансий с сайта HeadHunter.'''
    def __init__(self, page_size: int = 100, max_pages: int = 100):
        self.page_size = page_size
        self.max_pages = max_pages

    def load_vacancies(self, prompt: str) -> list[Vacancy]:
        '''Загружает вакансии с сайта HeadHunter по заданному запросу.
             prompt (str): Поисковый запрос для вакансий.
             Возвращает список объектов Vacancy, представляющих загруженные вакансии.
        '''
        vacancies = []
        url = 'https://api.hh.ru/vacancies'
        headers = {'User-Agent': 'HH-User-Agent'}
        for i in range(self.max_pages):
            params = {'text': prompt, 'page': i, 'per_page': self.page_size}
            response = requests.get(url, headers=headers, params=params)
            data = response.json().get("items", [])
            for item in data:
                try:
                    salary = item.get('salary', {})
                    snippet = item.get('snippet', {})
                    vacancies.append(Vacancy(
                        title=item['name'],
                        place=item['area']['name'],
                        salary_lower_limit=salary.get('from', 0) if salary else 0,
                        salary_upper_limit=salary.get('to', 0) if salary else 0,
                        salary_currency=salary.get('currency') if salary else 'RUR',
                        requirement=snippet.get('requirement', ''),
                        responsibility=snippet.get('responsibility', ''),
                    ))
                except Exception as e:
                    print(f'Warning: cannot validate HH vacancy: {e}')
        return vacancies
