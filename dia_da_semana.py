# Lê a entrada do usuário e converte para número inteiro
dia = int(input("Digite um número de 1 a 7: "))

# Estrutura condicional para verificar o dia correspondente
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