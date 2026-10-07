'''
crie um código em python que tese se o site Pudim está acessivel pelo computador usado
'''

print('==='*15)
print('EXERCICIOS 106'.center(44))
print('==='*15)
print(' ')

import requests

url = 'https://pudim.com.br/'

try:
    resposta = requests.get(url, timeout=5)
    resposta.raise_for_status()

except (
    requests.exceptions.ConnectionError,
    requests.exceptions.Timeout,
    requests.exceptions.HTTPError
):
    print('\033[0;31mSem acesso ao site!\033[m')

else:
    print('\033[0;32mO site ainda vive!\033[m')
