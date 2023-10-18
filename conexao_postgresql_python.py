import psycopg2

# Parâmetros de conexão com o banco de dados
nome_do_banco = 'dev_bacias'
usuario = 'postgres'
senha = 'cobrape'
host = 'localhost'
porta = '5432'

conn = psycopg2.connect(
    dbname = nome_do_banco,
    user = usuario,
    password = senha,
    host = host,
    port = porta
)

cur = conn.cursor()

# Realização de consulta SQL
cur.execute('SELECT cobacia '\
            'FROM ottobacias_tiete_bho_2017_5k '\
            'ORDER BY cobacia DESC')
result = cur.fetchall()

# Nome do arquivo de saída (pode conter um diretório específico)
arquivo_texto = "resultado_consulta.txt"

# Abrindo o arquivo .txt para escrever os resultados
with open(arquivo_texto, "w") as arquivo:
    for row in result:
        # Convertendo cada linha em uma string formatada e escrevendo no arquivo
        linha_formatada = "\t".join(map(str, row))  # Tabulação separando os valores
        arquivo.write(linha_formatada + "\n")  # Adição de quebra de linha

# Commit e fechando a conexão
conn.commit()
conn.close()

print(f"Resultados salvos em {arquivo_texto}")
