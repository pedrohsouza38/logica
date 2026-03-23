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