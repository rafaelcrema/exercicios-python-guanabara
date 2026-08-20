'''
CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA, MOSTRANDO UMA MENSAGEM NO FINAL,
DE ACORDO COM A MÉDIA ATINGIDA

- MEDIA ABAIXO DE 5.0: REPROVADO
- MEDIA ENTRE 5.0 E 6.9 RECUPERAÇÃO
- MEDIA 7.0 OU SUPERIOR APROVADO
'''

primeira_nota = float(input('Digite a sua primeira nota: \n>'))
segunda_nota = float(input('Digite sua segunda nota: \n>'))
media = (primeira_nota + segunda_nota) / 2

#If para separar notas
if media < 5.0:
    print('Sua nota é \033[31m{:.2}\033[m, infelizmente, você foi reprovado'.format(media))

elif media > 7.0:
    print('Sua nota é \033[32m{:.2}\033[m. Parabéns, até o proximo ano!'.format(media))

else:
    print('Sua nota é \033[33m{:.2}\033[m. Você esta de recuperação!'.format(media))