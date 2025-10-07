opcao = 0
while opcao != 3:
    print("\n1 - Contar até 10!")
    print("2 - Tabuada de um número")
    print("3 - Sair")
    opcao = int(input("Escolha: "))
    
    if opcao == 1:
        for i in range(1,11):
            print(i)
    elif opcao == 2:
        n = int(input("Número: "))
        for i in range(1,11):
            print(f"{n} x {n*i}")
    elif opcao == 3:
        print("Encerrando...")
    else:
        print("Opção inválida!")
