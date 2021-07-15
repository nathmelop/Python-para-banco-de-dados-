import random
n = int(input('Digite um numero entre 0 a 5:'))
aleatorio = random.randint(0,5)
print('o numero que o computador escolheu foi {}'.format(aleatorio))
if n == aleatorio:
    print('Parabéns você acertou!!!')
else:
    print('Você perdeu!!!')