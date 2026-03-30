# Programa de Tabuada Automatizado
# Desenvolvido para calcular tabuadas de 1 a 10 de qualquer número.

def calcular_tabuada():
    # 1. Entrada de Dados: Solicita o número ao usuário
    try:
        # A função input() lê o valor como texto (string), int() converte para número inteiro
        numero = int(input("Informe o número da tabuada: "))
        
        print(f"\nTabuada de {numero}:")
        print("-" * 15) # Apenas para formatação estética

        # 2. Estrutura de Repetição (for):
        # range(1, 11) gera uma sequência de 1 até 10 (o último número é exclusivo)
        for i in range(1, 11):
            resultado = numero * i
            
            # 3. Exibição formatada:
            # Uso de f-string para exibir o formato "x x n = res"
            print(f"{i} x {numero} = {resultado}")
            
        print("-" * 15)

    except ValueError:
        # Estrutura de decisão simples para garantir que o programa não quebre
        # caso o usuário digite letras em vez de números.
        print("Erro: Por favor, informe um número inteiro válido.")

# Executa a função
if __name__ == "__main__":
    calcular_tabuada()