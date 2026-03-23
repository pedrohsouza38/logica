# logica
Exercícios de Lógica com Python

1. Desenvolver um programa que leia o consumo de água para uma residência social e exiba o valor (R$) da conta baseado nos seguintes cálculos:
Se o consumo for menor ou igual a 10m3, então R$ 7,59
Se o consumo for menor ou igual a 20m3, então R$ 1,31 por m3
Se o consumo for menor ou igual a 30m3, então R$ 4,64 por m3
Se o consumo for menor ou igual a 50m3, então R$ 6,62 por m3
Se o consumo for acima dos 50m3, então R$ 7,31 por m3
residencia_social.py

consumo = float(input("Digite o consumo de água em m³: "))

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

consumo = float(input("Digite o consumo de água em m3: "))

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
    
calcular_conta_agua()

Justificar as estruturas de decisão

O uso da estrutura if-elif-else é fundamental por três motivos:

Exclusividade Mútua: O consumo de água não pode pertencer a duas faixas simultaneamente. Uma vez que uma condição é atendida (ex: consumo <= 10), as outras são descartadas, otimizando o processamento.

Hierarquia de Faixas: A estrutura elif permite testar os limites de forma sequencial. Como o código testa primeiro se o valor é menor que 10, no segundo teste (elif consumo <= 20) o programa já "sabe" implicitamente que o valor é maior que 10, dispensando verificações redundantes como if consumo > 10 and consumo <= 20.

Tratamento de Excedentes: O bloco else final funciona como um "capturador" para qualquer valor que não se enquadre nas regras anteriores (neste caso, qualquer valor estritamente maior que 50), garantindo que o programa sempre forneça uma resposta.

4. Desenvolver um programa que leia um número de 1 a 7 e exiba o dia da semana:
   1 - 'Domingo'
   2 - 'Segunda'
   3 - 'Terça'
   4 - 'Quarta'
   5 - 'Quinta'
   6 - 'Sexta'
   7 - 'Sábado'
Qualquer outro numero exibir: 'Opção inválida!'

dia = int(input("Digite um número de 1 a 7: "))

if dia == 1:

    print("Domingo")
    
elif dia == 2:

    print("Segunda")
    
elif dia == 3:

    print("Terça")
    
elif dia == 4:

    print("Quarta")
    
elif dia == 5:

    print("Quinta")
    
elif dia == 6:

    print("Sexta")
    
elif dia == 7:

    print("Sábado")
    
else:

    # Executado caso nenhuma das condições anteriores seja verdadeira
    
    print("Opção inválida!")

Justificativa das Estruturas de Decisão

Neste programa, utilize a estrutura if / elif / else:

if (Se): É a porta de entrada. O programa testa a primeira condição (se o número é 1).

elif (Senão se): Abreviação de else if. É ideal aqui porque os dias da semana são mutuamente exclusivos (um número não pode ser 2 e 3 ao mesmo tempo). Assim que o computador encontra uma condição verdadeira, ele ignora todas as seguintes, o que torna o código mais eficiente.

else (Senão): Funciona como um "filtro de segurança" ou caso padrão. Se o usuário digitar 0, 8 ou qualquer outro valor que não esteja mapeado, o else garante que o programa dê uma resposta clara (Opção inválida) em vez de simplesmente não fazer nada.

5. Desenvolver um programa que leia o peso e a altura de uma pessoa e calcule seu imc utilizando a fórmula: 
imc = peso / altura ^ altura
Com o imc exiba para o usuário seu imc e a classificação:
IMC		Classificação
< 16		'Magreza grave'
16 a < 17	'Magreza moderada'
17 a < 18,5	'Magreza leve'
18,5 a < 25	'Saudável'
25 a < 30	'Sobrepeso'
30 a < 35	'Obesidade Grau I'
35 a < 40	'Obesidade Grau II (severa)'
≥ 40		'Obesidade Grau III (mórbida)'

peso = float(input("Digite seu peso (kg): "))

altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.1f}")

if imc < 16:
    classificacao = "Magreza grave"
elif 16 <= imc < 17:
    classificacao = "Magreza moderada"
elif 17 <= imc < 18.5:
    classificacao = "Magreza leve"
elif 18.5 <= imc < 25:
    classificacao = "Saudável"
elif 25 <= imc < 30:
    classificacao = "Sobrepeso"
elif 30 <= imc < 35:
    classificacao = "Obesidade Grau I"
elif 35 <= imc < 40:
    classificacao = "Obesidade Grau II (severa)"
else: # IMC >= 40
    classificacao = "Obesidade Grau III (mórbida)"

print(f"Classificação: {classificacao}")

Justificativa das Estruturas de Decisão

As estruturas if, elif (else if) e else foram utilizadas para criar uma lógica de seleção exclusiva, onde apenas um dos cenários é verdadeiro para o valor de imc. 

Ordem Lógica: As faixas são verificadas em ordem crescente (< 16, depois < 17, etc.). Se o IMC for 15, a primeira condição (<16) é verdadeira, o programa classifica e pula todas as outras validações, otimizando o processo.

Múltiplas Condições: O uso de elif permite que o programa verifique diversas faixas de valores consecutivas de forma organizada.

Cenário Padrão (else): O else final captura automaticamente qualquer valor igual ou superior a 40 (Obesidade Grau III), garantindo que todo possível resultado de IMC seja classificado.

6. Desenvolva um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem formam um triângulo e se formarem exibir na tela se é equilátero, isósceles ou escaleno.

Sabemos que:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;


lado_a = float(input("Digite o valor do lado A: "))
lado_b = float(input("Digite o valor do lado B: "))
lado_c = float(input("Digite o valor do lado C: "))

if (lado_a + lado_b > lado_c) and (lado_a + lado_c > lado_b) and (lado_b + lado_c > lado_a):
    print("Os valores formam um triângulo: ", end="")
    
    # Estruturas de decisão para classificar o tipo de triângulo [3, 8]
    if lado_a == lado_b == lado_c:
        print("Equilátero (três lados iguais).")
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        print("Isósceles (dois lados iguais).")
    else:
        print("Escaleno (três lados diferentes).")
else:
    print("Os valores NÃO formam um triângulo.")

Justificativa das Estruturas de Decisão

if (principal): Utilizado para verificar a condição de existência do triângulo. Sem ele, poderíamos classificar valores inválidos (ex: 1, 1, 10).

if (Equilátero): Checa se todos os lados são iguais (a==b==c) logo após a verificação principal, pois é a condição mais restritiva.

elif (Isósceles): Caso não seja equilátero, verifica se pelo menos dois lados são iguais.

else (Escaleno): Se não for equilátero nem isósceles, a única opção restante é que todos os lados sejam diferentes.
