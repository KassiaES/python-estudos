class Livro:
    def __init__(self, titulo, editora, generos, exemplares, autores, max_renovacoes=0):
        self.titulo = titulo
        self.editora = editora
        self.generos = generos
        self.exemplares = exemplares  # Lista de exemplares
        self.autores = autores
        self.emprestado = False
        self.max_renovacoes = max_renovacoes
        self.renovacoes = 0

    def __str__(self):
        return (f"Titulo: {self.titulo}, Editora: {self.editora}, Generos: {', '.join(self.generos)}, "
                f"Exemplares Disponíveis: {len(self.exemplares)}, Autores: {', '.join(self.autores)}, "
                f"Renovações Permitidas: {self.max_renovacoes}")

    def emprestar(self):
        if self.exemplares:
            self.exemplares.pop()
            self.emprestado = True
            print(f"O livro '{self.titulo}' foi emprestado.")
        else:
            print(f"Não há exemplares disponíveis do livro '{self.titulo}' para empréstimo.")

    def devolver(self):
        self.exemplares.append('exemplar')  # Adiciona um exemplar de volta à lista
        self.emprestado = False
        self.renovacoes = 0  # Resetar renovações ao devolver
        print(f"O livro '{self.titulo}' foi devolvido.")

    def renovar(self):
        if self.renovacoes < self.max_renovacoes:
            self.renovacoes += 1
            print(f"O livro '{self.titulo}' foi renovado. Renovações restantes: {self.max_renovacoes - self.renovacoes}")
        else:
            print(f"O livro '{self.titulo}' atingiu o número máximo de renovações.")
