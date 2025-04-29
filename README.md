# Teste de Autômatos Finitos Determinísticos (v1.0)

### Script Python para testar Autômatos Finitos Determinísticos

## ⚙️ Como executar o projeto

Após clonar o projeto para a pasta desejada, acesse a pasta e instale as bibliotecas:
```bash
pip install -r requirements.txt
```

Com isso, basta executar o arquivo `index.py`:
```bash
python index.py
```

## 🧑‍💻 Utilizando o script
Você deverá passar as informações referentes do autômato que deseja testar na ordem e em um padrão específico:

### 1. Alfabeto
A lista de caracteres que o seu autômato aceita. O alfabeto deve ser adicionado na seguinte estrutura:
```
a, b, c, d
```

### 2. Números de estados
Quantos estados o seu autômato possui.

### 3. Estado inicial
Qual é o estado inicial do seu autômato e deve ser especificado por meio da letra `q` seguido do número do estado (iniciando a contagem do zero). <br>
Por exemplo, se seu autômato possui 5 estados e o inicial é o 1, coloque: `q0`

### 4. Estado(s) final(is)
Adicionar o estado final (ou finais, se houver mais de um) do seu autômato e deve ser especificado de maneira semelhante aos pontos 1 e 3, ex.:
```
q3, q5
```

### 5. Passagem de estados do autômato
Aqui vamos passar por cada um dos estados do seu autômato e verificar qual o próximo estado com base na entrada. Precisamos especificar a entrada e o estado de destino para cada caractere do alfabeto. <br>
Por exemplo: alfabeto {a, b, c}
```
>> Insira os caminhos para o estado q0:
a q3, b q7, c q1
```
Ou seja, quando o estado `q0` recebe `a` ele vai para `q3` e assim por diante.

### 6. Testar as palavras
Após toda essa configuração, basta inserir as palavras que deseja testar e o código irá realizar a verificação com base nas informações adicionadas pelo usuário. Quando desejar sair do programa, basta inserir `SAIR` para encerrar. Não houve necessidade de implementar verificação de entrada (especificado pelo professor).
<br>

Se preferir, você encontrará na pasta do projeto o arquivo `caso_de_teste.txt` que contém um autômato finito determinístico, basta adicionar as informações no programa e testar.
