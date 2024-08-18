
import psycopg2
class DBManager:
    """
    Класс для подключения к БД
    """
    def __init__(self, database_name: str, params: dict):
        self.conn = psycopg2.connect(dbname=database_name, **params)
        self.cur = self.conn.cursor()
        self.conn.autocommit = True

    def get_companies_and_vacancies_count(self):
        """
        Метод получает список всех компаний и количество вакансий у каждой компании
        """
        pass

    def get_all_vacancies(self):
        """
        Метод получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты
        и ссылки на вакансию
        """
        pass

    def get_avg_salary(self):
        """
        Метод получает среднюю зарплату по вакансиям
        """
        pass

    def get_vacancies_with_higher_salary(self):
        """
        Метод получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
        """
        pass

    def get_vacancies_with_keyword(self):
        """
        Метод получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python
        """
