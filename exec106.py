'''
FAÇA UM MINI SISTEMA QUE UTILIZE O INTERACTIVEHELP DO PYTHON.
O USUARIO VAI DIGITAR O COMANDO E O MANUAL VAI  APARECER.
QUANDO O USUARIO DIGITAR FIN, O PROGRAMA TERMINA

OBS: USAR CORES
'''

print('==='*15)
print('EXERCICIOS 106'.center(44))
print('==='*15)
print(' ')

def manual():

    while True:
        escolha = input('''Escolha uma função: 
FIM para o sistema!\n\n''').strip().upper()

        if escolha == 'FIM':
            texto = 'Fim do sistena'.strip()
            cont_txt = len(texto)+10
            print(f'\033[41m{texto.center(cont_txt)}\033[0m')

            break

        if 'FIM' not in escolha:
            escolha = escolha.lower()
            texto = f'Função {escolha}'
            cont_txt = len(texto)+10
        #COR HELP
            print('\033[43m')
            help(escolha)
            print('\033[m')


#CODIGO PRINCIPAL
texto ='Sistema de Ajuda PyHELP'
num_esp = len(texto) + 10
print('\033[42m=\033[m'*num_esp)
print(f'\033[42m{texto.center(num_esp)}\033[m')
print('\033[42m=\033[m'*num_esp)

manual()
