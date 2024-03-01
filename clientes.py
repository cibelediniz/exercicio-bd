import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

# Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). 

# Insira alguns registros de clientes na tabela.

# Selecione o nome e a idade dos clientes com idade superior a 30 anos.

# Calcule o saldo médio dos clientes.

# Encontre o cliente com o saldo máximo.

# Conte quantos clientes têm saldo acima de 1000.

# Atualize o saldo de um cliente específico.

# Remova um cliente pelo seu ID.

conexao.commit()
conexao.close
