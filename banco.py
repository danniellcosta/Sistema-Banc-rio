import textwrap

saldo = 0
usuarios = []
contas = []
    
def exibir_menu():
    print(""" 
                  BANCO
    ##################################
    # 1 - Ver Saldo                  #          
    # 2 - Depositar                  #
    # 3 - Sacar                      #
    # 4 - Criar Usuário              #
    # 5 - Criar Conta Corrente       #
    # 6 - Extrato                    #
    # 7 - Listar Contas              #
    # 8 - Sair                       #
    ##################################
          """)

def ver_saldo():
    global saldo
    print(f"Seu saldo atual é de R$ {saldo}")

def validar_opcao(opcao):
    if(opcao <= 0):
        print("Opcão Inválida!")
    elif(opcao > 8):
        print("Opcão Inválida!")
    else:
        print("Opção válida!\n")

def depositar(valor,extrato,/):
    if valor > 0:
        global saldo
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print(f"Deposito de {valor} realizado com sucesso!")
        return extrato
    else:
        print("Valor inválido!")
        return extrato


def sacar(*,valor,extrato):
    global saldo
    saldo -= valor
    extrato += f" saque:\tR$ {valor:.2f}\n" 
    print("Saque realizado com sucesso!")
    print(f"Saque de {valor} realizado com sucesso!")
    return extrato
   

def criar_usuario():
    global usuarios
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf):
    global usuarios
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta_corrente(numero_conta, agencia):
    global usuarios
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")




def mostrar_extrato(saldo,/,*,extrato):
    print("""
#################### EXTRATO #########################      
         """)
    
    print("Não foram realizados movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("######################################################")
    

def listar_contas():
    global contas
    
    if not contas:
        print("Não há contas para listar.")
        return
        
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    extrato = ""
    limite = 500
    

    while(1):
        exibir_menu()

        opcao = int(input("Selecione uma das opções acima: "))
        validar_opcao(opcao)

        match opcao:
            case 1:
                ver_saldo()
                continuar = input("Deseja realizar alguma outra tarefa? (s/n): ")
            
                if continuar == "s":
                    continue
                elif continuar == "n":
                    mostrar_extrato()
                    exit(1)
            case 2: 
                deposito = float(input("Digite o valor que deseja depositar: "))
                extrato = depositar(deposito,extrato)
                
                continuar = input("Deseja realizar alguma outra tarefa? (s/n): ")
                if continuar == "s":
                    continue
                elif continuar == "n":
                    mostrar_extrato()
                    exit(1)
            case 3:
                print(f"Você está na opção de sacar, você tem direito a {LIMITE_SAQUES} saques diários de no máximo R$ {limite}")
                saque = float(input("Digite o valor que deseja sacar: "))
                if saque > saldo:
                    print("Saldo insuficiente!")
                    continue
                elif LIMITE_SAQUES == 0:
                    print("Limite de saque excedido!")
                    continue
                elif saque > limite:
                    print("Valor máximo de saque é de R$500,00")
                    continue
                
                extrato = sacar(valor=saque,extrato=extrato)
                LIMITE_SAQUES -= 1
                
                continuar = input("Deseja realizar alguma outra tarefa? (s/n): ")
                if continuar == "s":
                    continue
                elif continuar == "n":
                    mostrar_extrato()
                    exit(1)
            case 4:
                criar_usuario()
            case 5:
                numero_conta = len(contas) + 1
                conta = criar_conta_corrente(numero_conta, AGENCIA)
                
                if conta:
                    contas.append(conta)
            case 6:
                mostrar_extrato(saldo,extrato=extrato)
                continuar = input("Deseja realizar alguma outra tarefa? (s/n): ")
                if continuar == "s":
                    continue
                elif continuar == "n":
                    break
            case 7:
                listar_contas()
                continuar = input("Deseja realizar alguma outra tarefa? (s/n): ")
                if continuar == "s":
                    continue
                elif continuar == "n":
                    mostrar_extrato()
                    exit(1)
            case 8:
                break

main()