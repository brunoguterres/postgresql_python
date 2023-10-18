import psycopg2

# Parâmetros de conexão
nome_do_banco = "postgres"
usuario = "postgres"
senha = "cobrape"
host = "localhost"  # Ou o endereço do seu servidor PostgreSQL
porta = "5432"  # Porta padrão do PostgreSQL

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

# Inserir dados na tabela
cur.execute("INSERT INTO exemplo (nome, valor) VALUES (%s, %s)", ("Item A", 100))
cur.execute("INSERT INTO exemplo (nome, valor) VALUES (%s, %s)", ("Item B", 200))
cur.execute("INSERT INTO exemplo (nome, valor) VALUES (%s, %s)", ("Item C", 300))

# Confirmar alterações e fechar
conn.commit()
conn.close()
