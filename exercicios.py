import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()


cursor.execute('CREATE TABLE usuarios')


conexao.commit()    
conexao.close 