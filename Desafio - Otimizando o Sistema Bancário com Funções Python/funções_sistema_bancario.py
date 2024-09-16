import textwrap

def menu():
    menu = """"\n
    ******* MENU *******
    Digite sua opção:
    [NCl] Novo Cliente
    [NC] Nova Conta
    [EC] Exibir Contas
    [D] Depositar
    [S] Sacar
    [E] Extrato
    [X] Fechar o programa
    ==> """
    return input(textwrap.dedent(menu))

def deposita(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de: R$ {valor:.2f}\n"
        print(f"Depósito de: R$ {valor:.2f}")
        
    else:
        print("O depósito falhou, pois o valor informado é inválido.")
    
    return saldo, extrato

def saca(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("O saque falhou, pois o valor informado é maior do que o saldo.")

    elif valor > limite:
        print("O saque falhou, pois o valor do saque excede o limite da conta.")

    elif numero_saques >= limite_saques:
        print("O saque falhou, pois o número limite de saques já foi atingido.")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque de: R$ {valor:.2f}\n"
        numero_saques +=1
        print(f"Saque de: R$ {valor:.2f}")
        
    else:
        print("O saque falhou, pois o número informado é inválido.")

def exibe_extrato(saldo, extrato):
    print("\n******* EXTRATO *******")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("*********************")

def cria_cliente(clientes):
    cpf = input("Informe o documento de identificação do cliente (somente números): ")
    cliente = filtra_cliente(cpf, clientes)

    if cliente:
        print("\n Já existe cliente com esse documento de identificação!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")

    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("*** Cadastro de cliente criado com sucesso! ***")

def filtra_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def cria_conta(agencia, numero_conta, clientes):
    cpf = input("Informe o documento de identificação do cliente (somente números): ")
    cliente = filtra_cliente(cpf, clientes)

    if cliente:
        print("*** Conta criada com sucesso! ***")
        return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}

    print("\n Cliente não encontrado, processo de criação de conta foi encerrado")    

def exibe_conta():
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    agencia = "0001"
    clientes = []
    contas = []
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    
    while True:
        opcao = menu()
        
        if opcao == "D":
            valor = float(input("Você escolheu Depósito. \nInforme o valor que deseja depositar: "))

            saldo, extrato = deposita(saldo, valor, extrato)
    
        elif opcao == "S":
            valor = float(input("Você escolheu Saque. \nInforme o valor que deseja sacar: "))
        
            saldo, extrato = saca(saldo = saldo, valor = valor, extrato = extrato, limite = limite, numero_saques = numero_saques, limite_saques = limite_saques)
    
        elif opcao == "E":
            exibe_extrato(saldo, extrato)
        
        elif opcao == "NCl":
            cria_cliente(clientes)
        
        elif opcao == "NC":
            numero_conta = len(contas) + 1
            conta = cria_conta(agencia, numero_conta, clientes)
        
            if conta:
                contas.append(conta)
        
        elif opcao == "EC":
            exibe_conta(contas)
    
        elif opcao == "X":
            break

        else:
            print("Operação inválida, por favor selecione uma opção válida.")

main()