# Solicitando o salário ao usuário
salario_atual = float(input("Digite o salário atual do funcionário: R$ "))

# Estrutura condicional para determinar o percentual de aumento
if salario_atual <= 1000:
    percentual = 20
elif salario_atual <= 1700:
    percentual = 15
elif salario_atual <= 2300:
    percentual = 10
else:
    percentual = 5

# Cálculos matemáticos
valor_aumento = salario_atual * (percentual / 100)
novo_salario = salario_atual + valor_aumento

# Exibição dos resultados formatados
print(f"\nSalário antes do reajuste: R$ {salario_atual:.2f}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário, após o aumento: R$ {novo_salario:.2f}")