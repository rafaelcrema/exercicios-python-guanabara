'''
EXC 39
FAÇA UM PROGRAMA QUE LEIA 3 LINHAS E DIGA SE ELE FORMA UM TRINGULO OU NÃO

REFORÇO DO DESAFIO 35 dos tringulos
ACRESCENTANDO O RESULTADO O RESULTADO DE QUE MOSTRA QUE TIPO DE TRINGULO SERA FORMADO

- EQUILATERO TODOS OS LADOS IGUAIS
- ISOSCELES DOIS LADOS IGUAS
- ESCALENO TODOS OS LADOS DIFERENTES
'''
print('---'*10)
print('Exercicio 42')
print('---'*10)
print(' ')

a = int(input('Digite a primeira reta: \n>'))
b = int(input('Digite a segunda reta: \n>'))
c = int(input('Digite a terceira reta: \n'))

if a + b > c and a + c > b and b + c > a:
    print('Você tem um triangulo')

    if a == b and a == c and b == c:
        print('E ele é um triangulo EQUILATERO, pois tem todas as partes iguais')

    elif a != b and a != c and b != c:
        print('E ele é um triangulo ESCALENO, pois tem todos os lados diferentes')

    else:
        print('E ele é um triangulo ISOSCELES, pois tem dois lados iguais')
else:
    print('Você não tem um triangulo')