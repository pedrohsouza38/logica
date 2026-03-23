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