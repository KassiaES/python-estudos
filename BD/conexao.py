'''
1.Crie uma tabela chamada "alunos" com os seguintes campos:id(inteiro),nome(texto),idade(inteiro)e curso(texto).
2.Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
3.Consultas Básicas. Escreva consultas SQL para realizar as seguintes tarefas:
    a)Selecionar todos os registros databela "alunos".
    b)Selecionar o nome e a idade dos alunos com mais de 20 anos.
    c)Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
    d)Contar o número total de alunos na tabela
4.Atualização e Remoção
    a)Atualize a idadede um aluno específico na tabela.
    b)Remova um aluno pelo seu ID.
5.Criar uma Tabela e Inserir Dados.
    Crie uma tabela chamada "clientes" com os campos:id(chaveprimária),nome(texto),idade(inteiro)e saldo(float).
    Insira alguns registros de clientes na tabela.
6.Consultas e Funções Agregadas
    Escreva consultas SQL para realizar as seguintes tarefas:
    a)Selecione o nome e a idade dos clientes com idade superior a 30 anos.
    b)Calcule o saldo médio dos clientes.
    c)Encontre o cliente como saldo máximo.
    d)Conte quantos clientes têm saldo acima de 1000.
7.Atualização e Remoção com Condições
    a)Atualize o saldo de um cliente específico.
    b)Remova um cliente pelo seu ID.
8.Junção de Tabelas
    Crie uma segunda tabela chamada "compras" com os campos: id(chaveprimária),cliente_id(chaveestrangeirareferenciandooiddatabela"clientes"),produto(texto)e valor(real).
    Insira algumas compras associadas a clientes existentes na tabela "clientes".
    Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
'''


import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (1, "Caio", 23, "Cinema")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (2, "Joana", 29, "Sociologia")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (3, "Marina", 45, "Medicina")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (4, "Amanda", 26, "Enfermagem")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (5, "Paula", 21, "Odontologia")')
# cursor.execute('UPDATE alunos SET curso="Engenharia" WHERE nome="Marina"')
# cursor.execute('UPDATE alunos SET curso="Engenharia" WHERE id=1')
# cursor.execute('DELETE FROM alunos WHERE id=3')

dados = cursor.execute('SELECT * FROM alunos')
count = 0
for aluno in dados:
    print(aluno)
    count += 1
print(f"O número total de alunos é {count}")

nomes = cursor.execute('SELECT nome,idade FROM alunos WHERE idade > 20')
for aluno in nomes:
    print(aluno)

engenheiros = cursor.execute('SELECT * FROM alunos WHERE curso="Engenharia" ORDER BY nome')
for aluno in engenheiros:
    print(aluno)

cursor.execute('''
    CREATE TABLE clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER,
        saldo REAL
    )
''')
clientes = [
    ('João', 35, 1500.0),
    ('Maria', 28, 2000.0),
    ('Pedro', 42, 1200.0),
    ('Ana', 25, 800.0),
    ('Carlos', 30, 3000.0)
]
cursor.executemany('INSERT INTO clientes (nome, idade, saldo) VALUES (?, ?, ?)', clientes)
for cliente in clientes:
    print(cliente)

# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos
cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')
resultados = cursor.fetchall()
for resultado in resultados:
    print(resultado)

# b) Calcule o saldo médio dos clientes
cursor.execute('SELECT AVG(saldo) FROM clientes')
saldo_medio = cursor.fetchone()[0]
print(f"O saldo médio dos clientes é: {saldo_medio}")

# c) Encontre o cliente com o saldo máximo
cursor.execute('SELECT nome, saldo FROM clientes ORDER BY saldo DESC LIMIT 1')
cliente_max_saldo = cursor.fetchone()
print(f"\nCliente com o saldo máximo: {cliente_max_saldo[0]} - Saldo: {cliente_max_saldo[1]:.2f}")

# d) Conte quantos clientes têm saldo acima de 1000
cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')
clientes_ricos = cursor.fetchone()[0]
print(f"Há {clientes_ricos} clientes com saldo acima de 1000")

cursor.execute('''
CREATE TABLE IF NOT EXISTS compras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    produto TEXT,
    valor REAL,
    FOREIGN KEY(cliente_id) REFERENCES clientes(id)
)
''')

# Inserindo algumas compras associadas a clientes existentes
compras = [
    (1, "Notebook", 2500.00),
    (2, "Smartphone", 1500.00),
    (3, "Televisão", 2000.00),
    (1, "Tablet", 1200.00),
    (4, "Fone de Ouvido", 200.00)
]

cursor.executemany('INSERT INTO compras (cliente_id, produto, valor) VALUES (?, ?, ?)', compras)

# Escrevendo uma consulta para exibir o nome do cliente, o produto e o valor de cada compra
cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM compras JOIN clientes ON compras.cliente_id = clientes.id')

compras_clientes = cursor.fetchall()
print("Nome do Cliente | Produto | Valor")
for compra in compras_clientes:
    print(f"{compra[0]} | {compra[1]} | {compra[2]:.2f}")

cursor.execute('DROP TABLE compras')
cursor.execute('DROP TABLE clientes')

conexao.commit()
conexao.close()
