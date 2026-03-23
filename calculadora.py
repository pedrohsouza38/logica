import math # Importa a biblioteca math para raiz quadrada

def calculadora():
    print("--- Calculadora Aritmética ---")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Raiz quadrada (1º número)")
    print("7 - Número par")
    print("8 - Número ímpar")
    
    # Recebe a opção do usuário
    opcao = input("\nEscolha a operação (1-8): ")

    # Estrutura de Decisão para validar se precisa de dois números ou apenas um
    if opcao in ('1', '2', '3', '4', '5'):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    elif opcao in ('6', '7', '8'):
        num1 = float(input("Digite o número: "))
        num2 = 0 # Define um valor padrão para operações unárias
    else:
        print("Opção inválida!")
        return

    # --- Estrutura de Decisão: match-case (Python 3.10+) ---
    # Justificativa: O match-case é ideal para menus, pois compara a 'opcao' 
    # com múltiplos valores possíveis de forma limpa e eficiente, funcionando 
    # como um "switch" em outras linguagens.
    match opcao:
        case '1':
            print(f"Resultado: {num1 + num2}")
        case '2':
            print(f"Resultado: {num1 - num2}")
        case '3':
            print(f"Resultado: {num1 * num2}")
        case '4':
            # Estrutura de Decisão interna para tratar erro de divisão por zero
            if num2 != 0:
                print(f"Resultado: {num1 / num2}")
            else:
                print("Erro: Divisão por zero não permitida.")
        case '5':
            print(f"Resultado: {num1 ** num2}")
        case '6':
            # Estrutura de Decisão interna para raiz de números negativos
            if num1 >= 0:
                print(f"Resultado: {math.sqrt(num1)}")
            else:
                print("Erro: Raiz quadrada de número negativo.")
        case '7':
            if num1 % 2 == 0:
                print(f"{num1} é par.")
            else:
                print(f"{num1} não é par.")
        case '8':
            if num1 % 2 != 0:
                print(f"{num1} é ímpar.")
            else:
                print(f"{num1} não é ímpar.")
        case _:
            print("Opção inválida!")

# Executa a calculadora
calculadora()