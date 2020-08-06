from abc import ABC, abstractmethod
from app.core.entities.user import User

 
class UserRepositoryInterface(ABC):

    @abstractmethod
    def add(self, user: User):
        pass

    @abstractmethod
    def find(self, id:str)->User:
        pass