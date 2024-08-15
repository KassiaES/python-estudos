from abc import ABC, abstractmethod
from datetime import datetime

class ItemEmprestavel(ABC):
    def __init__(self, titulo, exemplares, max_renovacoes=0):
        self._titulo = titulo
        self.exemplares = exemplares
        self.emprestado = False
        self.max_renovacoes = max_renovacoes
        self.renovacoes = 0
        self.registros = []

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        if isinstance(value, str) and value.strip():
            self._titulo = value
        else:
            raise ValueError("Título deve ser uma string não vazia.")

    def __str__(self):
        return (f"Titulo: {self.titulo}, Exemplares Disponíveis: {len(self.exemplares)}, "
                f"Renovações Permitidas: {self.max_renovacoes}")

    @abstractmethod
    def emprestar(self, usuario):
        if self.exemplares:
            self.exemplares.pop()
            self.emprestado = True
            data_emprestimo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            registro = {
                "usuario": usuario.nome,
                "data_emprestimo": data_emprestimo,
                "data_devolucao": None,
                "estado": "emprestado"
            }
            self.registros.append(registro)
            print(f"O item '{self.titulo}' foi emprestado para {usuario.nome} em {data_emprestimo}.")
        else:
            print(f"Não há exemplares disponíveis do item '{self.titulo}' para empréstimo.")

    @abstractmethod
    def devolver(self):
        self.exemplares.append('exemplar')  # Adiciona um exemplar de volta à lista
        self.emprestado = False
        self.renovacoes = 0  # Resetar renovações ao devolver
        data_devolucao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for registro in self.registros:
            if registro["estado"] == "emprestado":
                registro["data_devolucao"] = data_devolucao
                registro["estado"] = "devolvido"
                break
        print(f"O item '{self.titulo}' foi devolvido em {data_devolucao}.")

    @abstractmethod
    def renovar(self):
        if self.renovacoes < self.max_renovacoes:
            self.renovacoes += 1
            print(f"O item '{self.titulo}' foi renovado. Renovações restantes: {self.max_renovacoes - self.renovacoes}")
        else:
            print(f"O item '{self.titulo}' atingiu o número máximo de renovações.")
