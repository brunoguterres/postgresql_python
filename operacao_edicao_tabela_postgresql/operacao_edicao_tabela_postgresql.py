import psycopg2

# Parâmetros de conexão
nome_do_banco = "postgres"
usuario = "postgres"
senha = "cobrape"
host = "localhost"
porta = "5432"

# Conectar ao banco de dados
conn = psycopg2.connect(
    dbname = nome_do_banco,
    user = usuario,
    password = senha,
    host = host,
    port = porta
)

# Criar um cursor
cur = conn.cursor()

# Recuperar os valores da coluna "valor"
cur.execute("SELECT valor FROM exemplo")
valores = [row[0] for row in cur.fetchall()]

# Realizar operações na matriz
resultado = [valor * 2 for valor in valores]

# Atualizar os valores na tabela
for i, novo_valor in enumerate(resultado):
    cur.execute("UPDATE exemplo SET valor = %s WHERE id = %s", (novo_valor, i + 1))

# Commit e fechar a conexão
conn.commit()
conn.close()

print("Valores originais:", valores)
print("Resultado das operações:", resultado)
