# Entrada das quatro notas bimestrais
# Usamos float() para permitir números decimais
n1 = float(input("Digite a 1ª nota: "))
n2 = float(input("Digite a 2ª nota: "))
n3 = float(input("Digite a 3ª nota: "))
n4 = float(input("Digite a 4ª nota: "))

# Cálculo da média aritmética simples
media = (n1 + n2 + n3 + n4) / 4

# Estrutura de decisão para atribuir o conceito com base na média
if 9.0 <= media <= 10.0:
    conceito = "A"
elif 7.5 <= media < 9.0:
    conceito = "B"
elif 6.0 <= media < 7.5:
    conceito = "C"
elif 4.0 <= media < 6.0:
    conceito = "D"
else:
    conceito = "E"

# Estrutura de decisão para definir a situação (Aprovado/Reprovado)
# Se o conceito estiver entre A e C, o aluno passa.
if conceito in ["A", "B", "C"]:
    situacao = "APROVADO"
else:
    situacao = "REPROVADO"

# Exibição dos resultados conforme solicitado
print(f"\n--- Resultado Final ---")
print(f"Notas: {n1}, {n2}, {n3}, {n4}")
print(f"Média Final: {media:.1f}")
print(f"Conceito: {conceito}")
print(f"Situação: {situacao}")