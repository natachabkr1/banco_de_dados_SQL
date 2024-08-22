# criação de um banco de dados - conectando o python com ukma linguagem de banco de dados SQL, armazenando os dados

'''
import sqlite3    # importando a biblioteca sqllite

conexao = sqlite3.connect('banco')     # estou conectando o arquivo python com o arquivo do banco de dados que criei ex. 'banco'
cursor = conexao.cursor()   

cursor.execute('')    # início dos comandos


conexao.commit()    # significa que vão ser enviadas informações a partir daqui
conexao.close       # serve para não dar conflito, ele finaliza a execução
'''


import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()


#* CREATE - Criação de Tabela
# cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
## cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
## cursor.execute('CREATE TABLE gerentes(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')

#* ALTER - Aletração de Tabela
# # cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
# cursor.execute('ALTER TABLE USUARIO ADD COLUMN telefoni INT')
# cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')

#* DROP - Excluindo tabela completa
## cursor.execute('DROP TABLE produtos') - deletar toda a tabela

#* INSERT - Inserindo informações dos usuários
# cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (1, "Isadora", "França", "isa@gmail.com", 123456)')  # inserindo informações
# cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (2, "Natacha", "Pelotas", "nati@gmail.com", 123456)')
# cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (3, "Fernando", "Rio Grande", "fer@gmail.com", 123456)')

#* DELETE - deletar alguma informação
# cursor.execute('DELETE FROM usuario where id=1')   # deletar apenas alguma informação


#* SELECT - Visualizar informações
# dados = cursor.execute('SELECT * FROM usuario')  # criando uma variável "dados" e associando uma seleção - * visualize todas informações 
# dados = cursor.execute('SELECT nome FROM usuario WHERE id>2')  -> com condição: mostrando somente os nomes onde o id é maior que 2

# for usuario in dados:
#     print(usuario)

# conexao.commit()
# conexao.close


#* UPDATE - Atualização de Dados:
# dados = cursor.execute('SELECT * FROM usuario')  -> mostra todos usuarios cadastrados
# for usuario in dados:
#     print(usuario)

# cursor.execute('UPDATE usuario SET endereco="Rio Grande" WHERE nome= "Fernando"')
# conexao.commit()
# conexao.close

#* ORDER BY - Colocando em ordem alfabética 
# dados = cursor.execute('SELECT * FROM usuario ORDER BY nome')
# for usuario in dados:
#     print(usuario)

#* Colocando em ordem decrescente - DESC
# dados = cursor.execute('SELECT * FROM usuario ORDER BY nome DESC')
# for usuario in dados:
#     print(usuario)


# cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (1, "Isadora", "França", "isa@gmail.com", 123456)')
# cursor.execute('INSERT INTO gerentes(id, nome, endereco, email) VALUES (1, "Matheus", "Brasil", "biel@gmail.com")')
# conexao.commit()
# conexao.close


#* LIMIT 
# dados = cursor.execute('SELECT * FROM usuario LIMIT 2')
# for usuario in dados:
#     print(usuario)

# DISTINCT - retorna os valores únicos / diferentes
# dados = cursor.execute('SELECT DISTINCT * FROM usuario')
# for usuario in dados:
#     print(usuario)

# GROUP BY - agrupa informações 
# dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome')
# for usuario in dados:
#     print(usuario)

# GROUP BY - agrupa informações e HAVING
# dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome HAVING id>2')
# for usuario in dados:
#     print(usuario)


# JOIN's (retorna informações que estão combinadas em 2 tabelas ou mais)

# INNER JOIN - busca e junta as linhas que tem correspondência entre as tabelas
## Estamos selecionando todas as informações dos usuarios juntando também com gerentes onde o id do usuario é = ao id do gerente
# dados = cursor.execute('SELECT * FROM usuario  INNER JOIN gerentes ON usuario.id = gerentes.id')
# for usuario in dados:
#     print(usuario)

# conexao.commit()
# conexao.close 

# LEFT JOIN - retorna todas as linhas da tabela a esquerda e se houver, correspondentes a direita
# dados = cursor.execute('SELECT * FROM usuario  LEFT JOIN gerentes ON usuario.id = gerentes.id')
# for usuario in dados:
#     print(usuario)

# conexao.commit()
# conexao.close


# RIGHT JOIN - retorna todas as linhas da tabela a direita e se houver, correspondentes a esquerda
# dados = cursor.execute('SELECT * FROM usuario RIGHT JOIN gerentes ON usuario.id = gerentes.id')
# for usuario in dados:
#     print(usuario)

# conexao.commit()
# conexao.close

# FULL JOIN - Retorna todas as linhas das 2 tabelas, comparando as informações (1º a esquerda e depois a direita)
# dados = cursor.execute('SELECT * FROM usuario FULL JOIN gerentes ON usuario.id = gerentes.id')
# for usuario in dados:
#     print(usuario)

# conexao.commit()
# conexao.close

## SUB CONSULTAS

# vou selecionar todas as informações do usuário onde o nome do usuario esteja dentro da tabela gerentes
dados = cursor.execute('SELECT * FROM usuario WHERE nome IN (SELECT nome FROM gerentes)')
for usuario in dados:
    print(usuario)

conexao.commit()
conexao.close