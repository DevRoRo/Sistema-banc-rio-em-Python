def menu():
    menu="""
    MENU
    [d] - Depósitos

    [s] - Saques

    [e] - Extrato

    [q] - Sair
    """
    
    return menu

def depositar(valor_deposito):
    if valor_deposito>0:
        print("Depósito realizado com sucesso")
        return valor_deposito
    else:
        print("Valor inválido, tente novamente")

def sacar(saldo, valor_saque):
    if valor_saque>500:
        print("Valor máximo de saque excedido, tente novamente")
    
    elif valor_saque>saldo:
        print("Não há saldo suficiente para realizar o saque")

    else:
        print("Saque realizado com sucesso")
        return valor_saque

def extrato(deposito, saque, saldo):
    mensagem=("Histórico de depósitos")
    for depositos in deposito:
        mensagem+=(f"\nR$ {depositos:.2f}")
    mensagem+=("\nHistórico de saques")
    for saques in saque:
        mensagem+=(f"\nR$ {saques:.2f}")
    mensagem+=(f"\nSaldo da conta: R$ {saldo:.2f}")

    return mensagem
    
def main():

    deposito=[]
    saque=[]
    saldo=0.0
    limite_saque=0

    while True:

        print(menu())

        opcao=input()

        if opcao == "d":
            valor_deposito=float(input("Informe valor a ser depositado: "))
            resultado=depositar(valor_deposito)
            deposito.append(resultado)
            saldo+=resultado
            
        elif opcao == "s":
            if limite_saque>=3:
                print("Limite de saque diário excedido")
                continue
            else:
                valor_saque=float(input("Informe valor a ser sacado: "))
                resultado=sacar(saldo, valor_saque)
                if resultado:
                    saque.append(resultado)
                    saldo-=resultado
                else:
                    continue

        elif opcao == "e":
            if deposito != [] or saque != []:
                resultado=(extrato(deposito, saque, saldo))
                print(resultado)
            else:
                print("Não foi realizado nenhuma operação")
                continue
                
        elif opcao == "q":
            break

        else:
            print("Operação inválida, selecione uma das opções válidas")

main()

