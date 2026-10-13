import listacadastro



def cadastrar():

    #listacadastro.lista_cadastro.clear()

    print('==='*15)
    print('\033[0;32mCADASTRO DE PESSOA\033[m'.center(53))
    print('==='*15)
    print()

    while True:
        while True:
            nome = input('Digite o nome: ').strip().capitalize()
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
    print('\033[0;32mPESSOAS CADASTRADAS\033[m'.center(53))
    print('==='*15)
    print()

    for pessoa in listacadastro.lista_cadastro:
        print(F'Nome: {pessoa['Nome']:.<30} Idade:{pessoa['Idade']}')


    
