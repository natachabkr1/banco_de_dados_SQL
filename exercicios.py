import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

# 1. Criando tabela
# cursor.execute('CREATE TABLE alunos (id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')

# 2. Inserindo dados
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
dados = cursor.execute('DELETE FROM alunos WHERE id= 3')
for alunos in dados:
    print(alunos)

conexao.commit()    
conexao.close


# 5. Criar uma atbela e inserir dados
