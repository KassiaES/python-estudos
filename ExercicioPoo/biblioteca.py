from livro import Livro

livros = []

def biblioteca():
    while True:
        print("\nMenu da Biblioteca:")
        print("1. Adicionar Livro")
        print("2. Ver Livros")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("5. Renovar Empréstimo")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '0':
            break
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
            for livro in livros:
                if livro.titulo.lower() == titulo.lower():
                    livro.emprestar()
                    break
            else:
                print(f"Livro '{titulo}' não encontrado.")
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
        else:
            print("Opção inválida, tente novamente.")
