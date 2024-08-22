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


conexao.commit()    
conexao.close 