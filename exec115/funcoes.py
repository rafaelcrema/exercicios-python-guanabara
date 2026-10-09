import listacadastro



def cadastrar():

    #listacadastro.lista_cadastro.clear()

    print('==='*15)
    print('CADASTRO DE PESSOA'.center(44))
    print('==='*15)
    print()

    while True:
        while True:
            nome = input('Digite o nome: ').capitalize().strip()
            try:
                if not nome.replace(' ','').isalpha():
                    raise ValueError
                break

            except ValueError:
                print('\033[0;31mDigite um nome valido!\033[m')

        while True:
            idade = input('Digite a idade: ').strip()
            try:
                idade = int(idade)
                break
            
            except ValueError:
                print('\033[0;31mDigite uma idade Valida!\033[m')

        pessoa = {
            'Nome': nome,
            'Idade': idade
        }

        listacadastro.lista_cadastro.append(pessoa)
        
        listacadastro.salvar()

        desicao = input('Quer adastrar mais alguem? [S/N]').strip().upper()
        if desicao == 'N':
            break

def cadastrados():

    print('==='*15)
    print('PESSOAS CADASTRADAS'.center(44))
    print('==='*15)
    print()

    for pessoa in listacadastro.lista_cadastro:
        print(F'Nome: {pessoa['Nome']} Idade:{pessoa['Idade']}')


    
