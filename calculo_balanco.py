import csv, time

def ler_arquivo_csv(nome_arquivo_entrada):  # esta função realiza o procedimento de leitura do CSV e constroi uma MATRIZ
    matriz = []
    with open(nome_arquivo_entrada, 'r') as arquivo_entrada:
        leitor_csv = csv.reader(arquivo_entrada)
        for linha in leitor_csv:
            if linha[0] == 'cobacia':   # desconsidera primeira linha com titulos da tabela
                continue
            matriz.append(linha)
    return matriz

def reordena_matriz(matriz, coluna_ordem):  # esta função reordena a matriz original de acordo com o campo cobacia
    matriz = sorted(matriz, key=lambda x: x[coluna_ordem], reverse=True)   # "True" ordena do maior para o menor
    return matriz

def definir_cabeceiras(matriz, campo_cobacia, campo_cobaciajus):    # esta função defini quais cobacias são cabeceiras
    for i in range(len(matriz)):    # percorre cada linha da matriz na coluna 0
        for j in range(len(matriz)):    # percorre cada linha da matriz na coluna 1
            if matriz[i][campo_cobacia] in matriz[j][campo_cobaciajus]: # verifica se a cobacia está na coluna cobaciajus
                matriz[i].append('nao') # adiciona dado de "não" para cabeceira na última coluna
                break   # se encontrar em cobaciajus interrompe o laço
        if matriz[i][-1] != 'nao':  # se não tiver dado de "não" para cabeceira (última campo [-1]) assume que deve ser "sim"
            matriz[i].append('sim') # adiciona dado de "sim" para cabeceira na última coluna
    return matriz

def criar_campos(matriz):   # esta função cria campos novos na matriz que serão necessários no cálculo do balanço
    for linha in matriz:
        linha.append(0)  # adiciona um atributo "0" no final de cada linha - campo_vazao_montante
        linha.append(0)  # adiciona um atributo "0" no final de cada linha - campo_vazao_jusante
        linha.append('nao')  # adiciona um atributo "0" no final de cada linha - campo_deficit
        linha.append(0)  # adiciona um atributo "0" no final de cada linha - campo_valor_deficit
    return matriz

def calculo_balanco(matriz, campo_cabeceira, campo_disponibilidade, campo_captacao, campo_vazao_montante, campo_vazao_jusante, campo_deficit, campo_valor_deficit): #esta função realiza o cálculo do balanço
    for i in range(len(matriz)):
        if matriz[i][campo_cabeceira] == 'sim':
            matriz[i][campo_vazao_montante] = 0
            matriz[i][campo_vazao_jusante] = float(matriz[i][campo_disponibilidade])-float(matriz[i][campo_captacao])
        elif matriz[i][campo_cabeceira] == 'nao':
            for j in range(len(matriz)): # colocar um teste para finalizar laço após encontrar 2 COBACIAJUS
                if matriz[i][campo_cobacia] == matriz[j][campo_cobaciajus] :
                    matriz[i][campo_vazao_montante] = matriz[i][campo_vazao_montante]+matriz[j][campo_vazao_jusante]
            matriz[i][campo_vazao_jusante] = matriz[i][campo_vazao_montante]+float(matriz[i][campo_disponibilidade])-float(matriz[i][campo_captacao])
        if matriz[i][campo_vazao_jusante] < 0:
            matriz[i][campo_deficit] = 'sim'
            matriz[i][campo_valor_deficit] = matriz[i][campo_vazao_jusante]*-1
            matriz[i][campo_vazao_jusante] = 0
    return matriz

def criar_csv_resultado(matriz, nome_arquivo_resultado):
    with open(nome_arquivo_resultado, 'w', newline='') as arquivo_resultado_csv:
        escritor_resultado_csv = csv.writer(arquivo_resultado_csv)
        for linha in matriz:
            escritor_resultado_csv.writerow(linha)


##### EXECUÇÃO #####

tempo_inicio = time.time()
print('tempo_inicio:',tempo_inicio)
print('\n')

campo_cobacia = 0
campo_cobaciajus = 1
campo_disponibilidade = 2
campo_captacao = 3
campo_cabeceira = 4
campo_vazao_montante = 5
campo_vazao_jusante = 6
campo_deficit = 7
campo_valor_deficit = 8

nome_arquivo_entrada = 'C:/Users/brunoguterres/Desktop/traducao_calculo_balanco_VBA/dados_brutos_v3.csv'
matriz = ler_arquivo_csv(nome_arquivo_entrada)

matriz = reordena_matriz(matriz, campo_cobacia)

'''print('\n')
print('Matriz reordenada:\n')
for linha in matriz:
    print(linha)
print('\n')'''

matriz = definir_cabeceiras(matriz, campo_cobacia, campo_cobaciajus)
matriz = criar_campos(matriz)
matriz = calculo_balanco(matriz, campo_cabeceira, campo_disponibilidade, campo_captacao, campo_vazao_montante, campo_vazao_jusante, campo_deficit, campo_valor_deficit)
titulos = ['cobacia','cobaciajus','disponibilidade','captacao','cabeceira','v_montante','v_jusante','deficit','v_deficit']
matriz.insert(0,titulos) # insere titulos na primeira linha da matriz novamente para finalizar

'''print('Matriz Final:\n')
for linha in matriz:
    print(linha)
print('\n')'''

nome_arquivo_resultado = 'resultado_v3.csv'
criar_csv_resultado(matriz, nome_arquivo_resultado)
print('Arquivo .csv com o resultado gerado!!!')

tempo_fim = time.time()
print('tempo_inicio:',tempo_inicio)
print('\n')
tempo_exec = (tempo_fim-tempo_inicio)/60    #tempo em minutos

print('\n')
print('Tempo total de execução:', tempo_exec)
