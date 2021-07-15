numero = int(input('Digite um numero para saber se é par ou ímpar:'))
num_d = numero % 2

if num_d == 0:
    print('Numero é par')
else:
    print('Numero é Ímpar')