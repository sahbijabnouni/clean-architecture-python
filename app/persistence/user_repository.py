
from app.core.entities.user import User
from app.persistence.data_models import UserTable
from app.core.application.repository.user_repository_interface import UserRepositoryInterface
class UserRepository(UserRepositoryInterface):

    def add(self, user: User):
        UserTable.create(id=user.id, firstName=user.firstName, lastName=user.lastName, email=user.email)
    
    def find(self,id:str)->User:
        data=UserTable.get(UserTable.id == id)
        user=User(data.id,data.firstName,data.lastName,data.email)
        return user
