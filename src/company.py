class Company:
    """
    Класс для работы с компанией
    """
    __slots__ = ("employer_id", "name", "description", "site_url", "open_vacancies")

    def __init__(self, employer_id, name, description, site_url, open_vacancies):
        """
        Конструктор класса
        """
        self.employer_id = employer_id
        self.name = name
        self.description = description
        self.site_url = site_url
        self.open_vacancies = open_vacancies

    def __str__(self) -> str:
        """
        Представление данных ввиде строки
        """
        return (
            f"ID компании: {self.employer_id}\n"
            f"Название компании: {self.name}\n"
            f"Описание компании: {self.description}\n"
            f"URL адрес компании: {self.site_url}\n"
            f"Количество открытых вакансий: {self.open_vacancies}\n"
        )
