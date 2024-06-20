from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class VacanciesLoader(ABC):
    '''Абстрактный класс для загрузки вакансий с сайтов'''
    @abstractmethod
    def load_vacancies(self, prompt: str) -> list[Vacancy]:
        pass






