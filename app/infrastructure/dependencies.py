from app.core.application.repository.user_repository_interface import UserRepositoryInterface
from app.core.application.manager.user_manager import UserManager
from app.persistence.user_repository import UserRepository
from injector import singleton
def Configure(binder):
    binder.bind(UserManager,UserManager(UserRepository()), scope=singleton)
