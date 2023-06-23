from Biblioteca.classes.livro import Livro


class TestLivro:
    def test_verificar_preenchimento(self):
        livro1 = Livro(1, "Dom Casmurro", "Machado de Assis", "Literatura")
        preenchido1 = livro1.verificar_preenchimento()
        assert preenchido1 == True

        livro2 = Livro(2, "", "Gabriel García Márquez", "Ficção")
        preenchido2 = livro2.verificar_preenchimento()
        assert preenchido2 == False

        livro3 = Livro(3, "O Senhor dos Anéis", "", "Fantasia")
        preenchido3 = livro3.verificar_preenchimento()
        assert preenchido3 == False

        livro4 = Livro(4, "", "", "")
        preenchido4 = livro4.verificar_preenchimento()
        assert preenchido4 == False

    def test_verificar_categoria_valida(self):
        livro1 = Livro(1, "Dom Casmurro", "Machado de Assis", "Literatura")
        categoria_valida1 = livro1.verificar_categoria_valida()
        assert categoria_valida1 == True

        livro2 = Livro(2, "Sapiens", "Yuval Noah Harari", "Ciência")
        categoria_valida2 = livro2.verificar_categoria_valida()
        assert categoria_valida2 == False

        livro3 = Livro(3, "1984", "George Orwell", "Distopia")
        categoria_valida3 = livro3.verificar_categoria_valida()
        assert categoria_valida3 == False
