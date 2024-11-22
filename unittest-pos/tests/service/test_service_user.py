from src.models.user import User
from src.service.service_user import ServiceUser


class TestServiceUser:

    def test_add_user_sucesso(self):

        service = ServiceUser()
        resultado_esperado = "Usuário adicionado com sucesso!"

        resultado = service.add_user("Chico", "QA")

        assert resultado == resultado_esperado
        assert len(service.store.bd) == 1
        assert service.store.bd[0].name == "Chico"
        assert service.store.bd[0].job == "QA"

    def test_add_user_falha(self):

        service = ServiceUser()
        service.add_user("Chico", "QA")
        resultado_esperado = "Usuário já existe!"

        resultado = service.add_user("Chico", "QA")

        assert resultado == resultado_esperado
        assert len(service.store.bd) == 1


    def test_update_user_sucesso(self):

        service = ServiceUser()
        service.add_user("Chico", "QA")
        resultado_esperado = "Usuário atualizado com sucesso!"

        resultado = service.update_user("Chico", "Desenvolvedor")

        assert resultado == resultado_esperado
        assert service.store.bd[0].job == "Desenvolvedor"

    def test_update_user_falha(self):

        service = ServiceUser()
        resultado_esperado = "Usuário não encontrado!"

        resultado = service.update_user("Regiane", "Gerente")

        assert resultado == resultado_esperado

    def test_get_user_by_name_sucesso(self):

        service = ServiceUser()
        service.add_user("Chico", "QA")

        usuario = service.get_user_by_name("Chico")

        assert isinstance(usuario, User)
        assert usuario.name == "Chico"
        assert usuario.job == "QA"

    def test_get_user_by_name_falha(self):

        service = ServiceUser()
        resultado_esperado = "Usuário não encontrado!"

        resultado = service.get_user_by_name("Regiane")

        assert resultado == resultado_esperado

    def test_get_user_by_name_parametro_invalido(self):

        service = ServiceUser()
        resultado_esperado = "O nome deve ser uma string"

        resultado = service.get_user_by_name(123)

        assert resultado == resultado_esperado

