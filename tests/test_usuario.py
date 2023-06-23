from unittest import TestCase
from Biblioteca.classes.usuario import Usuario
from Biblioteca.classes.sistema import Sistema


class TestUsuario:
    def test_preenchimento_deve_ser_obrigatorio(self):
        esperado = True

        usuario_teste = Usuario(1, 'Teste', 'teste@gmail.com', '21999999999')
        resultado = usuario_teste.verificar_preenchimento()  # When-ação

        assert resultado == esperado  # Then-desfecho

    def test_quando_codigo_esta_duplicado(self):
        sistema = Sistema()

        usuario1 = Usuario(1, "João", "joao@example.com", "123456789")
        adicionado1 = sistema.adicionar_usuario(usuario1)
        assert adicionado1 == True

        usuario2 = Usuario(2, "Maria", "maria@example.com", "987654321")
        adicionado2 = sistema.adicionar_usuario(usuario2)
        assert adicionado2 == True

        usuario3 = Usuario(1, "Pedro", "pedro@example.com", "555555555")
        adicionado3 = sistema.adicionar_usuario(usuario3)
        assert adicionado3 == False
