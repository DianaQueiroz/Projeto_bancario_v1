def menu():
    menu='''
    ============ MENU ============
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    ==============================
    [nu] Novo Usuário
    ==============================
    [lc] Listar Contas
    [nc] Nova Conta
    ==============================
    [q]  Sair
    ==============================
    => '''
    return input(menu)    

def depositar(saldo,valor,extrato,/):
    if valor>0:
        saldo+=valor
        extrato+=f'Depósito: R$ {valor:.2f}\n'
        print('=== Depósito realizado com sucesso! ===')
        print(f'=== Saldo atual de: R${saldo:.2f} ===')
    else:
        print('@@@ Operação falhou! O valor informado é inválido! @@@')
    return saldo, extrato

def sacar(*,saldo,valor,extrato,limite,numero_saques,LIMITE_SAQUES):
    excedeu_saldo=valor>saldo
    excedeu_limite=valor>limite
    excedeu_saques=numero_saques>=LIMITE_SAQUES
    if excedeu_saldo:
            print('@@@ Operação falhou! Você não tem saldo suficiente. @@@')
    elif excedeu_limite:
        print('@@@ Operação falhou! O valor do saque excede o limite. @@@')
    elif excedeu_saques:
        print('@@@ Operação falhou! Número máximo de saques diários excedido. @@@')
    elif valor>0:
        saldo-=valor
        extrato+=f'Saque: R$ {valor:.2f}'
        print('=== Saque realizado com sucesso! ===')
        print(f'=== Saldo atual de: R${saldo:.2f} ===')
        numero_saques+=1
    else:
        print('@@@ Operação falhou! O valor informado é inválido! @@@')
    return saldo, extrato

def exibir_extrato(saldo,/,*, extrato):
    print('\n=========EXTRATO=========')
    # print('\nNão foram realizadas movimentações na conta.'if not extrato else extrato) #também funciona
    print('\nNão foram realizadas movimentações na conta.' if extrato=='' else extrato)
    print(f'\nSaldo: R$ {saldo:.2f}')
    print('\n=========================')
    
def criar_usuario():
    cpf=input('Informe o CPF (somente números):\n')
    usuario=0

    if usuario:
        print('@@@ Já existe um usuário com esse CPF! @@@')

    nome=input('Informe seu nome completo:\n')
    data_nascimento=input('Informe sua data de nascimento (dd-mm-aaaa):\n')
    endereco=input('Informe seu endereço (logradouro, número - bairro - cidade/sigla do estado):\n')

    print('=== Usuário cadastrado com sucesso! ===')

def criar_conta():
    cpf=input('Informe o cpf cadastrado:\n')
    usuario=0

    if usuario:
        print('=== Conta criada com sucesso! ===')
        return {'Nome: ':nome,'Data de nascimento: ':data_nascimento,'Endereço: ':endereco}
    else:
        print('@@@ Usuário não encontrado. Por favor cadastrar usuário. @@@')

def filtrar_usuario():
    usuarios_filtrados=[usuario for usuario in usuarios if usuarios['cpf']==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_contas():
    pass

def main():
    LIMTE_SAQUES=3
    AGENCIA='0001'

    saldo=0
    limite=500
    extrato=''
    numero_saques=0
    usuarios=[]
    contas=[]

    while True:
        opcao=menu()
        if opcao=='d':
            valor=float(input('Informe o valor do depósito:\nR$ '))
            depositar(saldo,valor,extrato)
        elif opcao=='s':
            valor=float(input('Informe o valor do saque:\nR$ '))
            sacar(saldo=saldo,valor=valor,extrato=extrato,limite=limite,numero_saques=numero_saques,LIMTE_SAQUES=LIMTE_SAQUES)
        elif opcao=='e':
            exibir_extrato(saldo,extrato=extrato)
        elif opcao=='nc':
            criar_conta()
        elif opcao=='lc':
            listar_contas()
        elif opcao=='nu':
            criar_usuario()
        elif opcao=='q':
            print('Obrigado pela preferência, volte sempre!')
            break
        else:
            print('@@@ Opção inválida! Por favor selecione novamente a operação desejada. @@@')