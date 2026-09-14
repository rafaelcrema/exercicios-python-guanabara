'''
FAÇA UM PROGRAMA QUE LEIA O NOME E A MÉDIA DE UM ALUNO.
GUARDE TAMBÉM A SITUAÇÃO EM UM DICIONARIO.
NO FINAL. MOSTRE O CONTEUDO DA ESTRUTÚRA NA TELA
'''

print('==='*15)
print('EXERCICIOS 90'.center(45))
print('==='*15)
print(' ')

alunos = {}
nome = {}
nota = {}

nome = input('Digite o nome do aluno: ').strip().capitalize()
alunos["nome"] = nome
nota = float(input(f'Digite a média do {alunos['nome']}: '))
alunos[nome] = {
    "nota": nota
}

if alunos[nome]["nota"] < 6:
    print(f'O aluno {nome}, teve média de {alunos[nome]['nota']} e foi \033[31mREPROVADOR\033[m')
else:
    print(f'O aluno {nome}, teve média de {alunos[nome]['nota']} e foi \033[32mAPROVADO\033[m')
