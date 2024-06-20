from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class VacanciesStorage(ABC):
    '''Абстрактный класс для хранения вакансий'''
    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass

    def add_vacancies(self, vacancies: list[Vacancy]) -> None:
        for vacancy in vacancies:
            self.add_vacancy(vacancy)


    @abstractmethod
    def get_all_vacancies(self) -> list[Vacancy]:
        pass

    @abstractmethod
    def clear(self):
        pass
