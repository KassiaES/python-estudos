from livro import Livro
from usuario import Usuario
from colorama import Fore, Style

livros = []

def adicionar_usuario(usuarios):
    nome = input("Nome do usuário: ")
    telefone = input("Telefone do usuário: ")
    nacionalidade = input("Nacionalidade do usuário: ")
    usuario = Usuario(nome, telefone, nacionalidade)
    usuarios.append(usuario)
    print(f"Usuário '{Fore.BLUE}{nome}{Style.RESET_ALL}' adicionado com sucesso!")

def biblioteca(usuarios):
    while True:
        print("\nMenu da Biblioteca:")
        print("1. Adicionar Livro")
        print("2. Ver Livros")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("5. Renovar Empréstimo")
        print("6. Adicionar Usuário")
        print("7. Ver Registros de Empréstimos")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '0':
            return True
        elif escolha == '1':
            titulo = input("Título do livro: ")
            editora = input("Editora do livro: ")
            generos = input("Gêneros do livro (separados por vírgula): ").split(", ")
            exemplares = int(input("Número de exemplares disponíveis: "))
            autores = input("Autores do livro (separados por vírgula): ").split(", ")
            max_renovacoes = int(input("Número máximo de renovações permitidas: "))
            exemplares_lista = ['exemplar' for _ in range(exemplares)]
            livros.append(Livro(titulo, editora, generos, exemplares_lista, autores, max_renovacoes))
            print(f"Livro '{titulo}' adicionado com sucesso!")
        elif escolha == '2':
            for livro in livros:
                print(livro)
        elif escolha == '3':
            titulo = input("Título do livro a ser emprestado: ")
            usuario_nome = input("Nome do usuário que está emprestando o livro: ").lower()
            usuario = next((u for u in usuarios if u.nome.lower() == usuario_nome), None)
            if usuario:
                for livro in livros:
                    if livro.titulo.lower() == titulo.lower():
                        livro.emprestar(usuario)
                        break
                else:
                    print(f"Livro '{titulo}' não encontrado.")
            else:
                print(f"Usuário '{usuario_nome}' não encontrado.")
        elif escolha == '4':
            titulo = input("Título do livro a ser devolvido: ")
            for livro in livros:
                if livro.titulo.lower() == titulo.lower():
                    livro.devolver()
                    break
            else:
                print(f"Livro '{titulo}' não encontrado.")
        elif escolha == '5':
            titulo = input("Título do livro a ser renovado: ")
            for livro in livros:
                if livro.titulo.lower() == titulo.lower():
                    livro.renovar()
                    break
            else:
                print(f"Livro '{titulo}' não encontrado.")
        elif escolha == '6':
            adicionar_usuario(usuarios)
        elif escolha == '7':
            for livro in livros:
                print(f"Registros de empréstimos para '{Fore.BLUE}{livro.titulo}{Style.RESET_ALL}':")
                for registro in livro.registros:
                    print(registro)
        else:
            print("Opção inválida, tente novamente.")
    return False
