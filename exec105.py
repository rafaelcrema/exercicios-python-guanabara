'''
FAÇA UM PROGRAMA QUE TENHA UM FUNÇÃO notas() que pode
receber varias notas de alunos e vai retornar um dicionario com as seguintes informações

- QUANTIDADE DE NOTAS
- A MAIOR NOTA
- A MENOR NOTA
- A MÉDIA DA TURMA
- A SITUAÇÃO(OPCIONAL)

ADICIONA TAMBÉM OS DOCSTRING DA FUNÇÃO
'''

print('==='*15)
print('EXERCICIOS 105'.center(44))
print('==='*15)
print(' ')

geral = {}

def notas(*resp, sit=False):

    '''
    => Função para notas de alunos
    Resp traz o número de notas e agresenta dentro do cionionario
    separando em notas, mais alta, menor, media 
    Sit = True ou False exite situação da Sala
    '''

    men_nota = 10
    max_nota = 0
    geral.update({'Notas': resp})

#VERIFICA E ANOTA MENOR NOTA
    for ver_notas in geral['Notas']:
        if ver_notas < men_nota:
            men_nota = ver_notas
            geral.update({'Menor nota': men_nota})

#VERIFICA E ADICIONA MAIOR NOTA
    for ver_nota in geral['Notas']:
        if ver_nota > max_nota:
            max_nota = ver_notas
            geral.update({'Maior Nota': max_nota})

#MEDIA DA SALA
    num_notas = len(geral['Notas'])
    soma = sum(geral['Notas'])
    media = soma / num_notas
    geral.update({'Média': round(media,1)})

#SITUAÇÃO
    if sit == True:
        if media <= 10:
            geral.update({'Situação': 'Excelente'})
        if media <=8:
            geral.update({'Situação': 'Boa'})
        if media <= 6:
            geral.update({'Situação': 'Mediana'})
        if media <= 4:
            geral.update({'Situação': 'RUIM'})
        
    return geral


#PROGRAMA PRINCIPAL
resp = notas(5.5, 2.2, 1.5, 6.5, sit=True)
print(resp)