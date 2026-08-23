'''
CIE UM PROGRAMA QUE LEIA UMA FRASE E DIGA SE ELE É UM PALINDROMO,
DESCONSIDERANDO OS ESPAÇOS
'''


print('==='*15)
print('EXERCICIOS 53'.center(45))
print('==='*15)
print(' ')

frase = input('Digite uma fase: \n>')
frase_junta = frase.replace(' ', '').lower()

frase_invertida = []

tamanho = len(frase_junta)

for posicao in range(tamanho -1, -1, -1):
    frase_invertida.append(frase_junta[posicao])

frase_invertida = "".join(frase_invertida).lower()

if frase_junta == frase_invertida:
    print(f'{frase} é um palindromo. \nFrase Normal {frase}\nFrase Invertida {frase_invertida}')
else:
    print(f'{frase} Não é um palindromo.\nFrase Normal {frase}\nFrase Invertida {frase_invertida}')
