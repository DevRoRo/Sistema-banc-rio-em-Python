
menu="""
MENU
[d] - Depósitos

[s] - Saques

[e] - Extrato

[q] - Sair
"""
deposito=[]
saque=[]
saldo=0.0
limite_saque=0

while True:

    opcao=input(menu)

    if opcao == "d":
        valor_deposito=float(input("Informe valor a ser depositado: "))
        deposito.append(valor_deposito)
        saldo+=valor_deposito

    elif opcao == "s":
        if limite_saque>=3:
            print("Limite de saque diário excedido")
            continue
        valor_saque=float(input("Informe valor a ser sacado: "))
        if valor_saque>500:
            print("Valor máximo de saque excedido, tente novamente")
            continue
        if valor_saque>saldo:
            print("Não há saldo suficiente para realizar o saque")
        saque.append(valor_saque)
        saldo+=valor_saque*-1
        limite_saque+=1

    elif opcao == "e":
        if deposito != [] or saque != []:
            print("Histórico de depósitos")
            for depositos in deposito:
                print(f"R$ {depositos:.2f}")
            print("Histórico de saques")
            for saques in saque:
                print(f"R$ {saques:.2f}")
            print(f"Saldo da conta: R$ {saldo:.2f}")     
        else:
            print("Não foi realizado nenhuma operação")
            continue
            
    elif opcao == "q":
        break

    else:
        print("Operação inválida, selecione uma das opções válidas")


