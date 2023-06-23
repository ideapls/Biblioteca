from datetime import date


class Usuario:
    def __init__(self, codigo, nome, email, telefone):
        self._codigo = codigo
        self._nome = nome
        self._email = email
        self._telefone = telefone

    @property
    def codigo(self):
        return self._codigo

    @property
    def nome(self):
        return self._nome

    @property
    def email(self):
        return self._email

    @property
    def telefone(self):
        return self._telefone

    def verificar_preenchimento(self):
        if not self._codigo or not self._nome or not self._email or not self._telefone:
            return False
        return True

    def __str__(self):
        return f'Usuario({self._nome}, {self._telefone}, {self._codigo})'


