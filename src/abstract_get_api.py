from abc import ABC, abstractmethod

class GetCompaniesAPI(ABC):
    """
    Абстрактный класс для получения вакансий с hh.ru
    """
    @abstractmethod
    def load_data(self):
        pass
