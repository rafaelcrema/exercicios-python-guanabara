'''
FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SÓ ACEITE OS VALORES M OU F
CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO NOVAMENTE ATÉ TER UM VALOR CORRETO
'''

print('==='*15)
print('EXERCICIOS 57'.center(45))
print('==='*15)
print(' ')

sexo = ['M','F']

while sexo != 'M' or sexo != 'F':
    informe = input('Digite o seu sexo com [M/F]\n').upper()
    if informe == 'M' or informe == 'F':
        informe = sexo
        print('Obrigado!')
        break
    else:
        print('Coloque a respsota correta, seu animal!')