class Usuario:
    def __init__(self, nome, telefone, nacionalidade):
        self.nome = nome
        self.telefone = telefone
        self.nacionalidade = nacionalidade

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Nacionalidade: {self.nacionalidade}"
