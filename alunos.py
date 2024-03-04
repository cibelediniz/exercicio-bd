import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

# Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).

cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

# Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Artur", 23, "Direito")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "Felipe", 31, "Políticas públicas")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "Victor", 28, "Tecnologia da Informação")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "Keila", 33, "Geografia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Bárbara", 25, "História")')

# Selecionar todos os registros da tabela "alunos".

todos_alunos = cursor.execute('SELECT * FROM alunos')

for alunos in todos_alunos:
    print(alunos)

# Selecionar o nome e a idade dos alunos com mais de 20 anos.

nome_idade = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')

for alunos in nome_idade:
    print(alunos)

# Selecionar os alunos do curso de "Engenharia" em ordem alfabética.

engenharia = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome')

for alunos in engenharia:
    print(alunos)

# Contar o número total de alunos na tabela

total_alunos = cursor.execute('SELECT COUNT(*) FROM alunos')

for alunos in total_alunos:
    print(alunos)

# Atualize a idade de um aluno específico na tabela.

nova_idade = cursor.execute('UPDATE alunos SET idade = 30 WHERE id = 2')

# Remova um aluno pelo seu ID.

cursor.execute('DELETE FROM alunos WHERE id = 5')

conexao.commit()
conexao.close
