menu = """"

Digite sua opção:

[D] Depositar
[S] Sacar
[E] Extrato
[X] Fechar o programa

==> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
   
    opcao = input(menu)

    if opcao == "D":
        valor = float(input("Você escolheu Depósito. \nInforme o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito de: R$ {valor:.2f}\n"
            print(f"Depósito de: R$ {valor:.2f}")
        
        else:
            print("O depósito falhou, pois o valor informado é inválido.")
    
    elif opcao == "S":
        valor = float(input("Você escolheu Saque. \nInforme o valor que deseja sacar: "))

        if valor > saldo:
            print("O saque falhou, pois o valor informado é maior do que o saldo.")

        elif valor > limite:
            print("O saque falhou, pois o valor do saque excede o limite da conta.")

        elif numero_saques >= LIMITE_SAQUES:
            print("O saque falhou, pois o número limite de saques já foi atingido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de: R$ {valor:.2f}\n"
            numero_saques +=1
            print(f"Saque de: R$ {valor:.2f}")
        
        else:
            print("O saque falhou, pois o número informado é inválido.")
    
    elif opcao == "E":
        print("\n-----EXTRATO-----")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("-----------------")
    
    elif opcao == "X":
        break

    else:
        print("Operação inválida, por favor selecione uma opção válida.")