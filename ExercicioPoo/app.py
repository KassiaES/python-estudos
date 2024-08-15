'''
Vamos criar um sistema orientado a objetos para representar um
sistema de biblioteca seguindo os requisitos abaixo:
1. Cada livro pode ter um ou mais autores.
2. A biblioteca controla apenas o nome, o telefone e a nacionalidade
de cada usuário.
3. Cada livro tem um título, editora, uma lista de gêneros aos quais
pertence e uma lista de exemplares disponíveis.
4. Quando um exemplar é emprestado, ele é removido da lista de
exemplares disponíveis.
5. Alguns livros podem ter um número máximo de renovações
permitidas.
6. A biblioteca mantém um registro de todos os empréstimos
realizados, incluindo detalhes como data de empréstimo, data de
devolução e estado do exemplar (por exemplo, emprestado ou
devolvido)
Para modelar o sistema, utilize obrigatoriamente os conceitos de classe,
herança, propriedade, encapsulamento e classe abstrata.
'''

from biblioteca import biblioteca, adicionar_usuario
from usuario import Usuario

usuarios = []

def menu():
    while True:
        usuario = input('Digite o seu nome de usuário ou 0 para sair do sistema: ').lower()
        if usuario == '0':
            print('Encerrando o sistema..')
            break
        elif usuario not in [user.nome.lower() for user in usuarios]:
            print('Usuário não encontrado. Deseja se cadastrar? (s/n)')
            resposta = input().lower()
            if resposta == 's':
                adicionar_usuario(usuarios)
        else:
            if biblioteca(usuarios):
                break

if __name__ == "__main__":
    menu()
