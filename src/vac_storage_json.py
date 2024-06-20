import json
from pathlib import Path

from src.vacancy import Vacancy
from src.vac_storage import VacanciesStorage


class JSONVacanciesStorage(VacanciesStorage):
    '''Класс для хранения вакансий в формате JSON'''
    def __init__(self, file_path: str | Path):
        self._file_path = Path(file_path)

    def _load_data(self) -> list:
        '''Загружает данные из JSON файла.
        Возвращает список словарей, представляющих данные о вакансиях'''
        if self._file_path.exists():
            with open(self._file_path, 'r') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []
        else:
            data = []
        return data

    def _save_data(self, data: list[dict]) -> None:
        '''Сохраняет данные в JSON файл'''
        with open(self._file_path, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    def add_vacancy(self, vacancies: list[Vacancy]) -> None:
        '''Добавляет список вакансий в хранилище'''
        data = self._load_data()
        for vacancy in vacancies:
            data.append(vacancy.to_dict())
        self._save_data(data)


    def get_all_vacancies(self) -> list[Vacancy]:
        '''Получает все вакансии из хранилища. Возвращает список объектов вакансий'''
        with open(self._file_path, 'r') as f:
            data = json.load(f)
        return [Vacancy.from_dict(item) for item in data]

    def clear(self):
        '''Очищает хранилище вакансий'''
        with open(self._file_path, 'w') as f:
            json.dump([], f)