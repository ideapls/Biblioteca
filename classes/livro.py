class Livro:
    CATEGORIAS_VALIDAS = ["Computação", "História", "Literatura", "Filosofia"]

    def __init__(self, codigo, titulo, autor, categoria):
        self._codigo = codigo
        self._titulo = titulo
        self._autor = autor
        self._categoria = categoria

    @property
    def codigo(self):
        return self._codigo

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def categoria(self):
        return self._categoria

    def verificar_preenchimento(self):
        if not self._codigo or not self._titulo or not self._autor or not self._categoria:
            return False
        return True

    def verificar_categoria_valida(self):
        if self._categoria not in self.CATEGORIAS_VALIDAS:
            return False
        return True