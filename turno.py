# Solicita ao usuário que insira o turno e converte para maiúsculas para facilitar a comparação
turno = input("Em que turno você estuda? (M-Matutino, V-Vespertino, N-Noturno): ").upper()

# Estrutura de decisão para verificar a opção digitada
if turno == 'M':
    # Se M, exibe Bom Dia
    print("Bom Dia!")
elif turno == 'V':
    # Se V, exibe Boa Tarde
    print("Boa Tarde!")
elif turno == 'N':
    # Se N, exibe Boa Noite
    print("Boa Noite!")
else:
    # Se nenhuma das opções acima, exibe Valor Inválido
    print("Valor Inválido!")