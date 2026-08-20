'''
FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM A SUA IDADE

- SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR
- SE É A HORA DE SE ALISTAR
- SE JÁ PASSOU DO TEMPO DE ALISTAMENTO

O PROGRAMA TAMBÉM DEVE MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO
'''

from datetime import date

print('-='*30)
print('Exercicio 39')
print('-='*30)
print()

ano_nascimento = int(input('Qual seu ano de nascimento: '))
ano_atual = date.today().year

anos_alistamento = ano_atual - ano_nascimento

# if que verifica se ele esta ou não na data de se alistar
if anos_alistamento < 18:
    print('Você ainda não precisa se alistar, faltam {} anos para isso!'.format(anos_alistamento))

elif anos_alistamento > 18:
    anos_mais = anos_alistamento - 18
    print('Você já se alistou a {} anos, seu Matusalen'.format(anos_mais))

else:
    print('Esta na hora de se alistar, vagabundo!')