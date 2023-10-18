import csv

def ler_arquivo_csv(nome_arquivo_entrada):  # esta função realiza o procedimento de leitura do CSV e constroi uma MATRIZ
    matriz = []
    with open(nome_arquivo_entrada, 'r') as arquivo_entrada:
        leitor_csv = csv.reader(arquivo_entrada)
        for linha in leitor_csv:
            if linha[1] == 'cobacia':   # desconsidera primeira linha com titulos da tabela
                continue
            matriz.append(linha)
    return matriz

def criar_campos(matriz):   # esta função cria campos novos na matriz que serão necessários no cálculo do balanço
    for linha in matriz:
        linha.append(0)  # adiciona um atributo "0" no final de cada linha da linha - campo_vazao_montante
        linha.append(0)  # adiciona um atributo "0" no final de cada linha da linha - campo_vazao_jusante

    return matriz

def calculo_balanco(matriz): #esta função realiza o cálculo do balanço
    for i in range(len(matriz)):
        if i%10000==0:
            print(i)
        mont = 0
        montante = 0
        if matriz[i][campo_cabeceira] == '1':
            matriz[i][campo_vazao_montante] = montante
        else:
            ini = i-1
            for j in range(ini,-1,-1):
                
                if matriz[i][campo_cotrecho] == matriz[j][campo_trechojus] :
                    montante += matriz[j][campo_vazao_jusante]
                    mont +=1
                  
                    if mont == 2:
                        break

        matriz[i][campo_vazao_jusante] = montante + float(matriz[i][campo_disponibilidade])
        matriz[i][campo_vazao_montante] = montante
       
    return matriz

def criar_csv_resultado(matriz, nome_arquivo_resultado):
    with open(nome_arquivo_resultado, 'w', newline='') as arquivo_resultado_csv:
        escritor_resultado_csv = csv.writer(arquivo_resultado_csv)
        for linha in matriz:
            escritor_resultado_csv.writerow(linha)


##### EXECUÇÃO #####

campo_cotrecho = 0  # vai ser o cotrecho
campo_cobacia = 1 # vai ser a cobacia
campo_trechojus = 2  # vai ser o ntutrjusante
campo_disponibilidade = 3  # vai ser a disponibilidade no caso 1
campo_cabeceira = 4 # cabeceira
campo_vazao_montante = 5 # montante
campo_vazao_jusante = 6  # jusante
campo_deficit = 7   # vazio
campo_valor_deficit = 8  # vazio

nome_arquivo_entrada = 'parana50000.csv'
matriz = ler_arquivo_csv(nome_arquivo_entrada)

matriz = criar_campos(matriz)
matriz = calculo_balanco(matriz)
titulos = ['cotrecho','cobacia','trecho jus','disponib','cabeceira','v_montante','v_jusante']
matriz.insert(0,titulos) # insere titulos na primeira linha da matriz novamente para finalizar

nome_arquivo_resultado = 'resultado50000.csv'
criar_csv_resultado(matriz, nome_arquivo_resultado)
print('Arquivo .csv com o resultado gerado!!!')