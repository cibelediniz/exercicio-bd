import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

# Crie uma segunda tabela chamada "compras"

# campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). 

# Insira algumas compras associadas a clientes existentes na tabela "clientes".

# Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra

conexao.commit()
conexao.close
