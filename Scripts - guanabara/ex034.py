salario = int(input('Qual é seu salario?'))
if salario > 1250:
    aumento = salario + (salario * 10 / 100)
else:
    aumento = salario + (salario * 15 / 100)
print('Seu salario agora é {}'.format(aumento))