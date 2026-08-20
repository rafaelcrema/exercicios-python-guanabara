'''ESCREVE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USUARIO ESCOLHER QUAL SERA A BASE DE CONVERSÃO
1 BINARIA
2 OCTAL
3 HEXADECIMAL'''

num_int = int(input('Digite um número inteiro: \n>'))


#função binaria
def binario(numero):
    if numero == 0:
        return '0'

    restos_bi = []

    while numero > 0:
        resto = numero % 2
        restos_bi.append(str(resto))
        numero = numero // 2

    return ''.join(restos_bi[::-1])

#função octal
def octal(numero):
    if numero == 0:
        return '0'

    restos_octal = []

    while numero > 0:
        resto_octal = numero % 8
        restos_octal.append(str(resto_octal))
        numero = numero // 8

    return ''.join(restos_octal[::-1])

#função hexadecimal
def hexa(numero):
    if numero == 0:
        return '0'

    hex_chars = '0123456789ABCDEF'
    restos_hex = []

    while numero > 0:
        resto = numero % 16
        restos_hex.append(hex_chars[resto])
        numero = numero // 16
    return ''.join(restos_hex[::-1])

escolha = input('Escolha qual a cionversão do seu número: \n[1] Binaria\n[2] Octal\n[3] Hexadecimal\n>')

#if de escolha dos parametros
if escolha == '1':
    resultado = binario(num_int)
    print('O número escolhido é {} e o Binario é {}'.format(num_int,resultado))
elif escolha == '2':
    resultado = octal(num_int)
    print('O número escolhido é {} e o Octal dele é {}'.format(num_int,resultado))
elif escolha == '3':
    resultado = hexa(num_int)
    print('O número escolhido é {} e o Hexadecimal é {}'.format(num_int,resultado))
else:
    print('Você passou uma opção invalida!')
                          