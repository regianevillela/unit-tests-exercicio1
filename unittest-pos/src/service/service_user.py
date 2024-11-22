from src.models.store import Store
from src.models.user import User


class ServiceUser:
    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):
        if name is None or job is None:
            return "O campo nome ou cargo não podem ser vazios para o usuário"
        if not isinstance(name, str) or not isinstance(job, str):
            return "O nome e o cargo devem ser strings"

        for user in self.store.bd:
            if user.name == name:
                return "Usuário já existe!"

        new_user = User(name, job)
        self.store.bd.append(new_user)
        return "Usuário adicionado!"

    def remove_user(self, name, job):
        for user in self.store.bd:
            if user.name == name:
                self.store.bd.remove(user)
                return "Usuário deletado!"
        return "Usuário não encontrado!"

    def update_user(self, name, new_job):
        if not isinstance(name, str) or not isinstance(new_job, str):
            return "O nome e o novo cargo devem ser strings"
        if name is None or new_job is None:
            return "O campo nome ou novo cargo não podem ser vazios"
        for user in self.store.bd:
            if user.name == name:
                user.job = new_job
                return "Usuário atualizado com sucesso!"
        return "Usuário não encontrado!"

    def get_user_by_name(self, name):
        if not isinstance(name, str):
            return "O nome deve ser uma string"
        if name is None:
            return "O campo nome não pode ser vazio"
        for user in self.store.bd:
            if user.name == name:
                return user

        return "Usuário não encontrado!"
