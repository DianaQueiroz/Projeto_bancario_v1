menu='''
=============
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=============
=> '''
saldo=0
limite=500
extrato=''
numero_saques=0

LIMITE_SAQUES=3

while True: 
    opcao=input(menu)

    if opcao=='d':
        valor=float(input('Informe o valor do depósito: \nR$ '))
        if valor>0:
            saldo+=valor
            extrato+=f'Depósito: R$ {valor:.2f}\n'
            print('Depósito realizado com sucesso!')
            print(f'Saldo atual de: R${saldo:.2f}')
        else:
            print('Operação falhou! O valor informado é inválido!')

    elif opcao=='s':
        valor=float(input('Informe o valor do saque: \nR$ '))
        excedeu_saldo=valor>saldo
        excedeu_limite=valor>limite
        excedeu_saques=numero_saques>=LIMITE_SAQUES
        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente.')
        elif excedeu_limite:
            print('Operação falhou! O valor do saque excede o limite.')
        elif excedeu_saques:
            print('Operação falhou! Número máximo de saques diários excedido.')
        elif valor>0:
            saldo-=valor
            extrato+=f'Saque: R$ {valor:.2f}'
            print('Saque realizado com sucesso!')
            print(f'Saldo atual de: R$ {saldo:.2f}')
            numero_saques+=1
        else:
            print('Operação falhou! O valor informado é inválido!')

    elif opcao=='e':
        print('\n=========EXTRATO=========')
        # print('\nNão foram realizadas movimentações na conta.'if not extrato else extrato) #também funciona
        print('\nNão foram realizadas movimentações na conta.' if extrato=='' else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('\n=========================')

    elif opcao=='q':
        print('Obrigado pela preferência, volte sempre!')
        break

    else:
        print('Opção inválida! Por favor selecione novamente a operação desejada.')