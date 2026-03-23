# --- Programa de Cálculo de Descontos (INSS e IRRF 2024) ---

def calcular_salario():
    # Leitura do Salário Bruto
    try:
        salario_bruto = float(input("Digite o valor do salário bruto (R$): "))
    except ValueError:
        print("Valor inválido. Utilize números.")
        return

    # --- 1. CÁLCULO INSS 2024 (Progressivo) ---
    # Tabela 2024: 7.5%, 9%, 12%, 14%
    inss = 0.0
    
    if salario_bruto <= 1412.00:
        inss = salario_bruto * 0.075
    elif salario_bruto <= 2666.68:
        inss = (salario_bruto * 0.09) - 21.18 # Fator de dedução
    elif salario_bruto <= 4000.03:
        inss = (salario_bruto * 0.12) - 101.18
    elif salario_bruto <= 7786.02:
        inss = (salario_bruto * 0.14) - 181.18
    else:
        inss = 908.85 # Teto do INSS 2024

    # --- 2. CÁLCULO IRRF 2024 (Base de cálculo = Bruto - INSS) ---
    base_irrf = salario_bruto - inss
    irrf = 0.0

    # Tabela IRRF 2024: Isento até R$ 2.259,20
    if base_irrf <= 2259.20:
        irrf = 0.0
    elif base_irrf <= 2826.65:
        irrf = (base_irrf * 0.075) - 169.44 # Alíquota e dedução
    elif base_irrf <= 3751.05:
        irrf = (base_irrf * 0.15) - 381.44
    elif base_irrf <= 4664.68:
        irrf = (base_irrf * 0.225) - 662.77
    else:
        irrf = (base_irrf * 0.275) - 896.00

    # --- 3. EXIBIÇÃO DOS RESULTADOS ---
    salario_liquido = salario_bruto - inss - irrf
    
    print("-" * 30)
    print(f"Salário Bruto:    R$ {salario_bruto:8.2f}")
    print(f"(-) INSS:         R$ {inss:8.2f}")
    print(f"(-) IRRF:         R$ {irrf:8.2f}")
    print(f"(=) Salário Liq.: R$ {salario_liquido:8.2f}")
    print("-" * 30)

# Executar a função
calcular_salario()