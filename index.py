import tabulate, pandas, os

def limpar():
    os.system('clear')

def imprimirAutomatoTable():
    # Impressao da tabela do automato formatada para melhor visualizacao
    limpar()
    print()
    df = pandas.DataFrame(estados)
    print(tabulate.tabulate(df.T, headers="keys", tablefmt="pretty"))

def testarPalavras():
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

alfabeto = ["a", "b", "c"]
nEstados = 8
inicial = "q0"
finais = "q3"
estados = {
    "q0": {"a": "q7", "b": "q7", "c": "q1"},
    "q1": {"a": "q7", "b": "q2", "c": "q7"},
    "q2": {"a": "q3", "b": "q7", "c": "q7"},
    "q3": {"a": "q6", "b": "q6", "c": "q4"},
    "q4": {"a": "q6", "b": "q5", "c": "q4"},
    "q5": {"a": "q3", "b": "q6", "c": "q4"},
    "q6": {"a": "q6", "b": "q6", "c": "q4"},
    "q7": {"a": "q7", "b": "q7", "c": "q7"}
}

limpar()
selecao = input("""<=== TESTADOR DE AUTÔMATO FINITO DETERMINÍSTICO ===>\n
Selecione uma opção:\n
1. Usar autômato de teste\n
2. Inserir um novo autômato\n
3. Sair\n
>> """)

opcao = int(selecao) if selecao.isdigit() else 3

if (int(opcao) == 1):
    imprimirAutomatoTable()
    print('Estado inicial: q0\nEstado final: q3')
    testarPalavras()
elif (int(opcao) == 2):
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

    imprimirAutomatoTable()
    testarPalavras()
