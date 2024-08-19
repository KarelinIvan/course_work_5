from typing import Any

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

    @classmethod
    def from_company_cls(cls, company_date) -> Any:
        """
        Метод возвращает экземпляр класса
        """
        if isinstance(company_date, dict):
            return cls(
                    company_date.get("id"),
                    company_date.get("name"),
                    company_date.get("description", "нет описания"),
                    company_date.get("site_url", "нет URL"),
                    company_date.get("open_vacancies", 0)
                )
        else:
            print("Ошибка: данные компании должны быть словарем")
            return None
