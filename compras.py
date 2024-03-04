import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

# Crie uma segunda tabela chamada "compras"
# campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). 

cursor.execute('''
    CREATE TABLE compras (
        id INT PRIMARY KEY,
        cliente_id INT,
        produto TEXT,
        valor REAL,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    )
''')

# Insira algumas compras associadas a clientes existentes na tabela "clientes".

compras = [
    (1, "Camiseta", 20.50),
    (2, "Calça", 35.75),
    (3, "Sapato", 50.20)
]

for compra in compras:
    cursor.execute('''
        INSERT INTO compras (cliente_id, produto, valor)
        VALUES (?, ?, ?)
    ''', compra)

# Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra

resultados = cursor.execute('''
    SELECT c.nome, co.produto, co.valor
    FROM clientes c
    JOIN compras co ON c.id = co.cliente_id
''')

for compra in resultados:
    nome_cliente, produto, valor_compra = compra  
    print("Cliente:", nome_cliente)
    print("Produto:", produto)
    print("Valor:", valor_compra)
    print()

conexao.commit()
conexao.close
