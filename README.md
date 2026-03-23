# logica
Exercícios de Lógica com Python

1. Desenvolver um programa que leia o consumo de água para uma residência social e exiba o valor (R$) da conta baseado nos seguintes cálculos:
Se o consumo for menor ou igual a 10m3, então R$ 7,59
Se o consumo for menor ou igual a 20m3, então R$ 1,31 por m3
Se o consumo for menor ou igual a 30m3, então R$ 4,64 por m3
Se o consumo for menor ou igual a 50m3, então R$ 6,62 por m3
Se o consumo for acima dos 50m3, então R$ 7,31 por m3
residencia_social.py

# Leitura do consumo de água (entrada do usuário)
consumo = float(input("Digite o consumo de água em m³: "))
# Estrutura condicional para determinar a tarifa
if consumo <= 10:
    # Taxa fixa para consumo até 10m³
    valor_conta = 7.59
elif consumo <= 20:
    # Cálculo por m³ para a segunda faixa
    valor_conta = consumo * 1.31
elif consumo <= 30:
    # Cálculo por m³ para a terceira faixa
    valor_conta = consumo * 4.64
elif consumo <= 50:
    # Cálculo por m³ para a quarta faixa
    valor_conta = consumo * 6.62
else:
    # Cálculo por m³ para consumo acima de 50m³
    valor_conta = consumo * 7.31
# Exibição do resultado formatado com duas casas decimais
print(f"O valor da conta de água é: R$ {valor_conta:.2f}")

Justificativa do uso das estruturas

Para este problema, a estrutura mais adequada é o if-elif-else (condicional encadeada) pelos seguintes motivos:

Exclusividade Mutua: O consumo de uma residência não pode pertencer a duas faixas de preço simultaneamente. Assim que o programa encontra a primeira condição verdadeira (por exemplo, consumo <= 10), ele executa o bloco correspondente e ignora todos os outros (elif e else), otimizando o processamento.

Organização por Faixas: A estrutura permite definir limites claros. Ao usar o elif, garantimos que o teste subsequente só será feito se o anterior falhar. Por exemplo, ao chegar em consumo <= 20, já sabemos implicitamente que o consumo é maior que 10, o que simplifica a lógica matemática.

Tratamento de Exceções: O uso do else ao final serve como uma "cláusula de escape" para qualquer valor que não se enquadre nas regras anteriores (neste caso, qualquer valor estritamente maior que 50).

2. Desenvolver um programa que leia o consumo de água para uma residência normal e exiba o valor (R$) da conta baseado nos seguintes cálculos:
Se o consumo for menor ou igual a 10m3, então R$ 22,38
Se o consumo for menor ou igual a 20m3, então R$ 3,50 por m3
Se o consumo for menor ou igual a 50m3, então R$ 8,75 por m3
Se o consumo for acima dos 50m3, então R$ 9,64 por m3
residencia_normal.py

# Leitura do consumo de água fornecido pelo usuário
consumo = float(input("Digite o consumo de água em m3: "))
# Estrutura de decisão para determinar o valor da conta
if consumo <= 10:
    # Faixa 1: Taxa mínima fixa
    valor_conta = 22.38
elif consumo <= 20:
    # Faixa 2: Valor por m3 para consumo até 20
    valor_conta = consumo * 3.50
elif consumo <= 50:
    # Faixa 3: Valor por m3 para consumo até 50
    valor_conta = consumo * 8.75
else:
    # Faixa 4: Valor por m3 para consumo acima de 50
    valor_conta = consumo * 9.64
# Exibição do resultado formatado com duas casas decimais
print(f"O valor da conta de água é: R$ {valor_conta:.2f}")

Justificativa das Estruturas de Decisão

O uso da estrutura if-elif-else (se-senão se-senão) é fundamental neste problema pelos seguintes motivos:

Seleção de Intervalos: O problema apresenta regras que mudam conforme o valor de uma variável. As estruturas condicionais permitem que o programa "decida" qual cálculo aplicar baseando-se no intervalo em que o consumo se encontra.

Exclusividade: Como os intervalos são mutuamente exclusivos (um valor de consumo não pode estar em duas faixas de preço diferentes ao mesmo tempo), o uso de elif garante que, assim que uma condição for atendida, o programa ignore as demais, tornando-o mais eficiente.

Hierarquia de Testes: A ordem dos testes (do menor para o maior) simplifica a lógica. Por exemplo, ao chegar no elif consumo <= 20, o programa já "sabe" que o valor é maior que 10, pois o primeiro if falhou.

3. Desenvolver um programa que leia o consumo de água para prédios comerciais e industriais e exiba o valor (R$) da conta baseado nos seguintes cálculos:
Se o consumo for menor ou igual a 10m3, então R$ 44,95
Se o consumo for menor ou igual a 20m3, então R$ 8,75 por m3
Se o consumo for menor ou igual a 50m3, então R$ 16,76 por m3
Se o consumo for acima dos 50m3, então R$ 17,46 por m3
comercio_industria.py

def calcular_conta_agua():
    # Solicita a entrada do usuário
    try:
        consumo = float(input("Digite o consumo de água em m³: "))
    except ValueError:
        print("Por favor, insira um valor numérico válido.")
        return
    # Estrutura de decisão para determinar o valor da conta
    # Faixa 1: Consumo mínimo (Taxa fixa)
    if consumo <= 10:
        valor_conta = 44.95
    # Faixa 2: Consumo entre 10.1 e 20 m³
    elif consumo <= 20:
        valor_conta = consumo * 8.75
    # Faixa 3: Consumo entre 20.1 e 50 m³
    elif consumo <= 50:
        valor_conta = consumo * 16.76
    # Faixa 4: Consumo acima de 50 m³
    else:
        valor_conta = consumo * 17.46
    # Exibe o resultado formatado
    print(f"O valor da conta para um consumo de {consumo}m³ é: R$ {valor_conta:.2f}")
# Executa a função
calcular_conta_agua()

Justificar as estruturas de decisão

O uso da estrutura if-elif-else é fundamental por três motivos:

Exclusividade Mútua: O consumo de água não pode pertencer a duas faixas simultaneamente. Uma vez que uma condição é atendida (ex: consumo <= 10), as outras são descartadas, otimizando o processamento.

Hierarquia de Faixas: A estrutura elif permite testar os limites de forma sequencial. Como o código testa primeiro se o valor é menor que 10, no segundo teste (elif consumo <= 20) o programa já "sabe" implicitamente que o valor é maior que 10, dispensando verificações redundantes como if consumo > 10 and consumo <= 20.

Tratamento de Excedentes: O bloco else final funciona como um "capturador" para qualquer valor que não se enquadre nas regras anteriores (neste caso, qualquer valor estritamente maior que 50), garantindo que o programa sempre forneça uma resposta.
   6 - 'Sexta'
   7 - 'Sábado'
Qualquer outro numero exibir: 'Opção inválida!'

