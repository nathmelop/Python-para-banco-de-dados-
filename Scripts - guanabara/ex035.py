r1 = float(input('Digite o comprimento da primeira reta:'))
r2 = float(input('Digite o comprimento da segunda reta:'))
r3 = float(input('Digite o comprimento da terceira reta:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com os valores acima você PODE formar um triangulo!!')
else:
    print('Com os valores acima você NÃO pode formar um triangulo!!')
