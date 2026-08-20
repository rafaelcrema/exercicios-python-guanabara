#estudo para calcular financiamento
print('==='*20)
print('Calculo de financiamento')
print('==='*20)

renda = float(input("Digite seu salario: \n>"))
valor_casa = float(input("Digite o valor da casa que você quer comprar: \n>"))
anos = int(input("Em quantos anos você pretende pagar a casa? \n>"))

meses_pagando = anos * 12
prestacao_mensal = valor_casa / meses_pagando
limite_seguro = renda * 0.30
porcentagem_real = (prestacao_mensal / renda) * 100

if porcentagem_real < 30:
    print('Seu financiamento foi aprovado!')
    
else:
    print('Seu funanciamento foi recusado!')