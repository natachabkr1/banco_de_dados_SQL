import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

# 1. Criando tabela alunos 
# cursor.execute('CREATE TABLE alunos (id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')

# 2. Inserindo dados - pelo menos 5 registros
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Gabriel", 19, "Fisioterapia")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "Matheus", 14, "Fundamental")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "João", 21, "Música")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "Gisele", 18, "Química")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Márcia", 19, "Física")')

# 3. Consultas Básicas
# a) Selecionar todos os registros da tabela alunos
# dados = cursor.execute('SELECT * FROM alunos')
# for alunos in dados:
#     print(alunos)

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos
# dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
# for alunos in dados:
#     print(alunos)

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética
# dados = cursor.execute('SELECT curso FROM alunos WHERE curso = "Engenharia"')
# for alunos in dados:
#     print(alunos)

# d) Contar o número total de alunos na tabela
# dados = cursor.execute('SELECT COUNT(id) FROM alunos')
# for alunos in dados:
#     print(alunos)

# conexao.commit()    
# conexao.close 


# 4. Atualização e Remoção
# a) Atualize a idade de um aluno específico na tabela
# dados = cursor.execute('UPDATE alunos SET idade= 19 WHERE nome= "Gisele"')
# for alunos in dados:
#     print(alunos)

# conexao.commit()    
# conexao.close 


# b) Remova um aluno pelo seu ID
# dados = cursor.execute('DELETE FROM alunos WHERE id= 3')
# for alunos in dados:
#     print(alunos)

# conexao.commit()    
# conexao.close


# 5. Criar uma tabela e inserir dados - clientes

#cursor.execute('CREATE TABLE clientes (id INT, nome VARCHAR(100), idade INT, saldo FLOAT)')

# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(1, "João", 30, 1000.00)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(2, "Maria", 25, 500.00)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(3, "Joana", 28, 2000.00)')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(4, "Paula", 23, 1500.00)')

# conexao.commit()    
# conexao.close

# 6. Consultas e Funções Agregadas para as tarefas:
# a)Selecione o nome e a idade dos clientes com idade superior a 28 anos
# dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 28')
# for clientes in dados:
#     print(clientes)

# conexao.commit()    
# conexao.close

# b) Calcule o saldo médio dos clientes
# dados = cursor.execute('SELECT AVG(saldo) FROM clientes')
# for clientes in dados:
#     print(clientes)

# conexao.commit()    
# conexao.close

# c)Encontre o cliente com o saldo máximo

# dados = cursor.execute('SELECT nome FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)')
# for clientes in dados:
#     print(clientes)

# conexao.commit()    
# conexao.close

# d)Conte quantos clientes têm saldo acima de 1000

# dados = cursor.execute('SELECT COUNT(id) FROM clientes WHERE saldo > 1000')
# for clientes in dados:
#     print(clientes)

# conexao.commit()
# conexao.close

# 7.Atualização e Remoção com Condições
# a)Atualize o saldo de um cliente específico
# dados = cursor.execute('SELECT COUNT(id) FROM clientes WHERE saldo > 1000')
# for clientes in dados:
#     print(clientes)

# conexao.commit()
# conexao.close
 
# b)Remova um cliente pelo seu ID
# dados = cursor.execute('DELETE FROM clientes WHERE id= 2')
# for clientes in dados:
#     print(clientes)

# conexao.commit()
# conexao.close


# 8. Junção de Tabelas
# Crie uma segunda tabela chamada "compras" com os campos: id (chaveprimária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). 
# Insira algumas compras associadas a clientes existentes na tabela "clientes". 
# Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra

# Craindo tabela "compras" e associando a tabela clientes
# cursor.execute('CREATE TABLE compras (id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id))')

# conexao.commit()
# conexao.close

# Inserindo dados associado a tabela clientes
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(1, 1, "Café", 5.00)')
# cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(2, 4, "Açúcar", 3.00)')

# conexao.commit()
# conexao.close


# Consulta para exibir o nome do cliente, o produto e o valor de cada compra
dados = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM clientes INNER JOIN compras ON clientes.id = compras.cliente_id')
for clientes in dados:
    print(clientes)

conexao.commit()
conexao.close