import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

# Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). 

cursor.execute('CREATE TABLE clientes(id INT, nome VARCHAR(100), idade INT, saldo FLOAT);')

# Insira alguns registros de clientes na tabela.

cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(1, "Pedro", 21, 150.30)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(2, "Mariana", 31, 206.10)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(3, "Cecilia", 42, 300.01)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(4, "Zeca", 18, 20.50)')

# Selecione o nome e a idade dos clientes com idade superior a 30 anos.

idade30 = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')

for clientes in idade30:
    print(clientes)

# Calcule o saldo médio dos clientes.

saldo_medio = cursor.execute('SELECT AVG(saldo) AS saldo_medio FROM clientes')

for clientes in saldo_medio:
    print(clientes)

# Encontre o cliente com o saldo máximo.

saldo_max = cursor.execute('SELECT * FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)')

for clientes in saldo_max:
    print(clientes)

# Conte quantos clientes têm saldo acima de 1000.

saldo1000 = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')

for clientes in saldo1000:
    print(clientes)

# Atualize o saldo de um cliente específico.

cursor.execute('UPDATE clientes SET saldo = 1050.2 WHERE id = 2')

# Remova um cliente pelo seu ID.

cursor.execute('DELETE FROM clientes WHERE id = 3')

conexao.commit()
conexao.close
