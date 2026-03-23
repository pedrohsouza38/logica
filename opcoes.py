# --- Programa de Menu de Opções ---

# 1. Exibir o menu na tela
print("1 - Opção 1")
print("2 - Opção 2")
print("3 - Opção 3")
print("4 - Sair")

# 2. Ler a opção do usuário
opcao = input("Digite uma opção: ")

# 3. Estrutura de Decisão para verificar a opção
if opcao == '1':
    print("Você selecionou a opção 1")
elif opcao == '2':
    print("Você selecionou a opção 2")
elif opcao == '3':
    print("Você selecionou a opção 3")
elif opcao == '4':
    print("Você selecionou sair")
else:
    # Se nenhuma das anteriores for verdadeira, exibe erro
    print("Opção inválida!!!")

# 4. Finalizar o programa
print("Fim do programa!")