a = int(input('digite o primeiro numero:'))
b = int(input('Digite o segundo numero:'))
c = int(input('Digite o terceiro numero:'))
if a < b and a < c:
    menor = a
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c
print('Menor valor digitado foi o {}'.format(menor))

# Maior valor
if a > b and a > c:
    maior = a
if b > c  and b > a:
    maior = b
if c > a and c > b:
    maior = c
print('Maior valor digitado foi o {}'.format(maior))