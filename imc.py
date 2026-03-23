# Solicitando os dados de entrada do usuário
# O peso é recebido como número de ponto flutuante (float)
peso = float(input("Digite seu peso (kg): "))
# A altura é recebida em metros (ex: 1.75)
altura = float(input("Digite sua altura (m): "))

# Cálculo do IMC: Peso dividido pela altura elevada ao quadrado
imc = peso / (altura ** 2)

# Exibindo o valor do IMC calculado com uma casa decimal
print(f"Seu IMC é: {imc:.1f}")

# Estrutura de decisão para classificação do IMC
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

# Exibindo a classificação final
print(f"Classificação: {classificacao}")