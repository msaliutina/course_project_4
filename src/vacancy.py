class Vacancy:
    '''Класс, который работает с такими параметрами из вакансий как название вакансии,
    локация, зарплата, валюта зарплаты, требования, обязанности'''
    def __init__(self,
                 title: str,
                 place: str = '',
                 salary_lower_limit: int = 0,
                 salary_upper_limit: int = 0,
                 salary_currency: str = 'RUR',
                 requirement: str = '',
                 responsibility: str = ''):
        self.title = title
        self.place = place
        self.salary_lower_limit = salary_lower_limit
        self.salary_upper_limit = salary_upper_limit
        self.salary_currency = salary_currency
        self.requirement = requirement
        self.responsibility = responsibility
        self.validate()

    def validate(self):
        '''Метод для валидации атрибутов'''
        assert isinstance(self.title, str), 'Title should be str'
        assert bool(self.title), 'Title should be not empty'
        assert isinstance(self.place, str)
        assert isinstance(self.salary_lower_limit, int), 'Salary lower limit should be int'
        assert isinstance(self.salary_upper_limit, int), 'Salary upper limit should be int'
        assert isinstance(self.salary_currency, str), 'Currency should be str'
        assert isinstance(self.requirement, str), 'Requirement should be str'
        assert isinstance(self.responsibility, str), 'Responsibility should be str'

    def __eq__(self, other) -> bool:
        '''Переопределение оператора сравнения =='''
        return (
                self.title == other.title
                and self.place == other.place
                and self.salary_lower_limit == other.salary_lower_limit
                and self.salary_upper_limit == other.salary_upper_limit
                and self.salary_currency == other.salary_currency
                and self.requirement == other.requirement
                and self.responsibility == other.responsibility
        )

    def __str__(self):
        '''Переопределение метода str()'''
        return (f'Вакансия: {self.title}. Место: {self.place}. Зарплата нижняя: {self.salary_lower_limit}. '
                f'Зарплата верхняя: {self.salary_upper_limit}. Валюта: {self.salary_currency}.' 
                f'Требования: {self.requirement}. Ответственности:  {self.responsibility}')

    def __repr__(self):
       return f'{self.__str__()}'

    def __gt__(self, other) -> bool:
        '''Переопределение оператора > для сравнения зарплат'''
        if self.salary_currency != other.salary_currency:
            raise ValueError('Нельзя сравнить зарплаты разных валют')
        return self.salary_upper_limit > other.salary_upper_limit

    def to_dict(self):
        '''Метод для преобразования объекта в словарь'''
        return {
            'title': self.title,
            'place': self.place,
            'salary_lower_limit': self.salary_lower_limit,
            'salary_upper_limit': self.salary_upper_limit,
            'salary_currency': self.salary_currency,
            'requirement': self.requirement,
            'responsibility': self.responsibility,
        }

    @classmethod
    def from_dict(cls, data: dict):
        '''Метод класса для создания объекта Vacancy из словаря'''
        return cls(
            title=data.get('title', ''),
            place=data.get('place', ''),
            salary_lower_limit=data.get('salary_lower_limit', 0),
            salary_upper_limit=data.get('salary_upper_limit', 0),
            salary_currency=data.get('salary_currency', 'RUR'),
            requirement=data.get('requirement', ''),
            responsibility=data.get('responsibility', ''),
        )
