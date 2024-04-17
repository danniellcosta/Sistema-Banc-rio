saldo = 0;
qtd_saques = 3;
extrato = "";

while(1):
    
    print("""
###################################
# Bem-Vindo ao sua conta bancária #
# 1 - Ver saldo                   # 
# 2 - Sacar                       # 
# 3 - Depositar                   #
# 4 - Ver Extrato                 # 
# 5 - Sair                        # 
###################################
      """);

    opcao = int(input("Selecione uma opção dentre as mostrada acima: "));
    
    if opcao == 1:
        
        print(f"Seu saldo é de R${saldo}");
        
        continuar = input("Deseja realizar alguma outra tarefa? (s/n): ");
        
        if continuar == "s":
            continue;
        
        elif continuar == "n":
            
            print("\nNão foram realizadas movimentações." if not extrato else extrato);
            print(f" Saldo: R$ {saldo:.2f}"); 
            
            print("Obrigado por utilizar nosso sistema!");
            
            exit(1);
        else:
            print("Opção inválida!");
            continue;
        
    elif opcao == 2:
        
        print(f"Você está na opção sacar, você tem direito a {qtd_saques} saques diários de no máximo R$500.");
        saque = float(input("Digite o valor que deseja sacar: "));
        
        if saque > saldo:
            print("Saldo insuficiente!");
            continue;
        
        elif saque < 0:
            print("Valor inválido!");
            continue;
        
        elif saque > 500:
            print("Você não tem direito a sacar mais de R$500 por dia!");
            continue;
        
        if qtd_saques == 0:
            print("Você não tem direito a mais saques!");
            continue;
        
        saldo = saldo - saque;
        extrato += f" saque: R$ {saque:.2f} ";
        qtd_saques -= 1;
        
        print("Saque realizado com sucesso!");
        print(f"Seu saldo é de R${saldo:.2f}");
        
        continuar = input("Deseja realizar alguma outra tarefa? (s/n): ");
        
        if continuar == "s":
            continue;
        
        elif continuar == "n":
            
            print("\nNão foram realizadas movimentações." if not extrato else extrato);
            print(f" Saldo: R$ {saldo:.2f}"); 
            
            print("Obrigado por utilizar nosso sistema!");
            
            exit(1);
            
        else:
            print("Opção inválida!");
            continue;
        
    elif opcao == 3:
        
        deposito = float(input("Digite o valor que deseja depositar: "));
        
        if deposito < 0:
            print("Valor inválido!");
            continue;
        
        saldo = saldo + deposito;
        extrato += f"\n Depósitos: R$ {deposito:.2f} \n"
        
        print("Depósito realizado com sucesso!");
        print(f"Seu saldo é de R${saldo:.2f}");
        
        continuar = input("Deseja realizar alguma outra tareda? (s/n): ");
        
        if continuar == "s":
            continue;
        
        elif continuar == "n":
            
            print("\nNão foram realizadas movimentações." if not extrato else extrato);
            print(f" Saldo: R$ {saldo:.2f}"); 
            
            print("Obrigado por utilizar nosso sistema!");
            
            exit(1);
            
        else:
            print("Opção inválida!");
            continue;
        
    elif opcao == 4:
             
        print("\nNão foram realizadas movimentações." if not extrato else extrato);
        print(f" Saldo: R$ {saldo:.2f}"); 
        
    elif opcao == 5:
        
        print("\nNão foram realizadas movimentações." if not extrato else extrato);
        print(f" Saldo: R$ {saldo:.2f}"); 
        
        print("Obrigado por utilizar nosso sistema!");
        
        exit(1);
        
    else:
        print("Opção inválida!");
        continue;