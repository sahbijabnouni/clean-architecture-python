
from app.core.entities.user import User
from app.core.application.repository.user_repository_interface import UserRepositoryInterface
import uuid
from injector import inject
class UserManager:

    def __init__(self, user_repository_interface: UserRepositoryInterface):

        self.user_repository_interface = user_repository_interface

    def add(self, user: User):
        self.user_repository_interface.add(user)

    def find(self, id: str)->User:
        return self.user_repository_interface.find(id)