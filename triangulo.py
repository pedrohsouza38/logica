# Solicitando os lados do triângulo
lado_a = float(input("Digite o valor do lado A: "))
lado_b = float(input("Digite o valor do lado B: "))
lado_c = float(input("Digite o valor do lado C: "))

# Estrutura de decisão para verificar se formam um triângulo
# A soma de dois lados deve ser maior que o terceiro lado [2, 5]
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