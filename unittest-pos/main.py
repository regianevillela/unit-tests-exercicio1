from src.models.user import User
from src.service.service_user import ServiceUser

service = ServiceUser()

resultado = service.add_user("Chico","QA")
print(resultado)
print(service.store.bd[0].name)
print(service.store.bd[0].job)

resultado = service.remove_user("Chico", "QA")
print(resultado)

usuario = service.get_user_by_name("Chico")
print(usuario.name if isinstance(usuario, User) else usuario)

usuario = service.get_user_by_name("Regiane")
print(usuario)

resultado = service.add_user("Regiane", "Gerente")
print(resultado)

usuario = service.get_user_by_name("Regiane")
print(usuario.name if isinstance(usuario, User) else usuario)

resultado = service.update_user("Chico", "Desenvolvedor")
print(resultado)
print(service.store.bd[0].name)
print(service.store.bd[0].job)

resultado = service.update_user("Regiane", "Gerente")
print(resultado)

resultado = service.add_user("Jefferson", "QA Lead")
print(resultado)
print(service.store.bd[1].name)
print(service.store.bd[1].job)

resultado = service.update_user("Jefferson", "Gerente")
print(resultado)
print(service.store.bd[1].name)
print(service.store.bd[1].job)

# Remover
resultado = service.remove_user("Jefferson", "Gerente")
print(resultado)
