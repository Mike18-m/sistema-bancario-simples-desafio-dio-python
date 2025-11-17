import textwrap

def menu():
    menu = """\n
    ========= MENU =========
    [de]\tDepositar
    [sa]\tSacar
    [ex]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [qu]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n Depósito realizado com sucesso!")
    else:
        print("\n  O valor informado é invalido! Tente novamente.")

    return saldo, extrato
    
def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print(" Operação falhou! Saldo Insuficiente.")
    
    elif excedeu_limite:
        print("Operação falhou! O valor excede o limite disponível")

    elif excedeu_saques:
        print(" Operação falhou! Quantidade de saques excedido")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")

    else:
        print("O valor informado é inválido. Tente novamente")

    return saldo, extrato
           
def exibir_extrato(saldo, /, *, extrato):
    print("========== EXTRATO============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("==============================")
    
def criar_novo_usuario(usuarios):
    cpf = input("Por favor informe seu CPF (Apenas os números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(" Usuário já cadastrado")
        return

    nome = input(" Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input(" Informe o seu endereço (logradouro, número - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereço":endereco})
    print(" Usuário cadastrado com sucesso!")    

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None    

def criar_nova_conta(agencia, numero_conta, usuarios):
    cpf = input("informe o seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta":numero_conta, "usuario":usuario}
    
    print("Usuário não encontrado!")
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            c/c:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"    
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "de":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao =="sa":
            valor = float(input("Informe o valor de saque "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                limite_saques=LIMITE_SAQUES,
                numero_saques=numero_saques,
        )

        elif opcao =="ex":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao =="nu":
            criar_novo_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_nova_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)


        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "qu":
            break

        else:
            print("A operação selecionada é inválida, por favor verifique e selecione novamente.")

main()