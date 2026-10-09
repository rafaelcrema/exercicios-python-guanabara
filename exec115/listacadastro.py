lista_cadastro = []



def carregar():
    try:
        with open('cadastro.txt', 'r') as arquivos:
            for linha in arquivos:
                nome, idade = linha.strip().split(';')

                pessoa = {
                    'Nome': nome,
                    'Idade': idade
                }

                lista_cadastro.append(pessoa)

    except FileNotFoundError:
        pass


def salvar():
    with open('cadastro.txt', 'w') as arquivo:
        for pessoa in lista_cadastro:
            arquivo.write(f'{pessoa['Nome']};{pessoa['Idade']}\n')
