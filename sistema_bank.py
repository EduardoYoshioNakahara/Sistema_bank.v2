import os

def exibir_menu():
    os.system('cls')  
    print("""
*****************************************************
***************seja bem-vindo ao bank****************
*****************************************************
""")
    print('''
             1 - sacar
             2 - depositar
             3 - visualizar extrato
             0 - sair
             ''')

def sacar(saldo):
    valor_sacar = float(input('insira o valor que deseja sacar: '))
    if valor_sacar > saldo:
        print('Saldo insuficiente.')
    else:
        saldo -= valor_sacar
        print(f'Saque de R${valor_sacar:.2f} realizado com sucesso.')
    return saldo

def depositar(saldo):
    valor_depositar = float(input('insira o valor que deseja depositar: '))
    saldo += valor_depositar
    print(f'Depósito de R${valor_depositar:.2f} realizado com sucesso.')
    return saldo

def visualizar_extrato(saldo):
    print(f'Seu saldo é R${saldo:.2f}')
    input('aperte enter para sair')

def main():
    saldo = 1000
    while True:
        exibir_menu()
        opcao = int(input('insira a opção desejada: '))
        if opcao == 1:
            saldo = sacar(saldo)
        elif opcao == 2:
            saldo = depositar(saldo)
        elif opcao == 3:
            visualizar_extrato(saldo)
        elif opcao == 0:
            print('saindo..')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()
