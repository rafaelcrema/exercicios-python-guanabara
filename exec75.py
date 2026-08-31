'''
desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:

[A] quantas vezes aparece o valor 9
[B] Em que posição foi digitado o primeiro valor 3
[C] Quais foram os números pares
'''

print('==='*15)
print('EXERCICIOS 75'.center(45))
print('==='*15)
print(' ')

tupla = ()
nove = 0
par = ()
posicao = ()

cont = 0

while cont < 4:
    num = int(input('Digite um número: '))
    tupla = tupla + (num, )
    cont += 1

for procura in tupla:
    if procura == 9:
        posicao = tupla.index(procura)

for p in tupla:
    if p % 2 == 0:
        par = par + (p,)

print(f'A tupla é: {tupla}')

if posicao == ():
    print('O 9 não aparece em posição nenhuma')
else:
    print(f'O nove apareceu na posição {posicao + 1}')

print(f'O números pares são: {par}')
