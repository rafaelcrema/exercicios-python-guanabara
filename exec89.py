'''
CRIE UM PROGRAMA QUE LEIA NOME E DUAS NOTAS DE CARIOS ALUNOS E GUARDE TUDO RM UMA LISTA COMPOSTA.
NO FINAL, MOSTRE UM BOLETIM  CONTENDO A MÉDIA DE CADA UM E PERMITA QUE O USUARIO POSSA MOSTRAR AS NOTAS DE
CADA ALUNO INDIVIDUALMENTE
'''

print('==='*15)
print('EXERCICIOS 89'.center(45))
print('==='*15)
print(' ')

alunos = []
nome = []
nota = []

while True:
    select = input('''
Escolha as opções:
[1]Cadastrar aluno
[2]Mostrar média dos alunos
[3]Mostrar nota do aluno
[4]Sair
''').strip()
    if select == '1':
        while True:
            #cadastro de alunos
            nome_aluno = input('Informe o nome do aluno: ').capitalize().strip()
            nome.append(nome_aluno)

            #cadastrando a nota de cada aluno
            for n in range(2):
                nota_aluno = float(input(f'Digite a nota {n +1} do {nome_aluno}: '))
                nota.append(nota_aluno)

            nome.append(nota[:])
            alunos.append(nome[:])
            nota.clear()
            nome.clear()
            
            add_mais = input('Quer cadastrar mais alunos? [S/N]').strip().upper()
            if add_mais == 'N':
                break

    elif select == '2':
        for aluno in alunos:
            media = sum(aluno[1]) / len(aluno[1])
            if media >= 6:
                print(f'{aluno[0]}, \033[32m{media} APROVADO\033[m')
            else:
                print(f'{aluno[0]}, \033[31m{media} REPROVADO\033[m')

    elif select == '3':
        for aluno in alunos:
            print(aluno[0])

        opcao = input('Escolha o Aluno: ').strip().capitalize()
        for aluno in alunos:
            if aluno[0] == opcao:
                print(f'Aluno: {aluno[0]} | Nota 1: {aluno[1][0]} | Nota 2: {aluno[1][1]}')

    elif select == '4':
        break