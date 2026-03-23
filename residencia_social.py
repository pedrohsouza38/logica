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