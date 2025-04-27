import tabulate, pandas, os

os.system('clear')

# GET ALFABETO
alfabeto = input('Digite o alfabeto separado por vírgulas: ').replace(' ', '').strip().split(',')

# GET QTD DE ESTADOS
nEstados = int(input('\nDigite a quantidade de Estados: ').strip())

# GET ESTADO INICIAL
inicial = input('\nDigite qual o estado inicial (ex: q0): ').strip()

# GET ESTADOS FINAIS
finais = input('\nDigite quais os estados finais separados por vírgulas (ex: q1, q2): ').replace(' ', '').strip().split(',')

# DEFINE ESTADOS
estados = {}

for i in range(nEstados):
    entrada = input(f"\nInsira os caminhos para o estado q{i} no modelo [entrada destino] separados por vírgula (ex.: a q2, b q3, etc.): ").strip().split(',')

    temp = {}

    for j in entrada:
        chavDest = j.strip().split(" ")
        chave = chavDest[0]
        destino = chavDest[-1]
        temp.update({chave: destino})

    estados.update({f"q{i}": temp})

# Impressao da tabela do automato formatada para melhor visualizacao
print()
df = pandas.DataFrame(estados)
print(tabulate.tabulate(df.T, headers="keys", tablefmt="pretty"))

# TESTE DE PALAVRAS
print(f'\nDigite "SAIR" para encerrar a entrada de palavras')
while True:
    palavra = input(f"\nDigite uma palavra: ")

    if palavra == 'SAIR':
        break

    estadoAtual = "q0"

    for letra in palavra:
        estadoAtual = estados[estadoAtual][letra]

    if estadoAtual in finais:
        print('\nPalavra Aceita!')
    else:
        print('\nPalavra Recusada!')
