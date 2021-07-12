#16 

num = float(input('Digite um numero que sera arendondado:'))
print('O numero {} tem a parte inteira {}'.format(num,round(num)))

#17

co = float(input('Qual o valor do cateto oposto?'))
ca = float(input('Qual o valor do cateto adjacente?'))
hip = (co ** 2  + ca ** 2 ) ** (1/2)
print('O valor do cateto oposto é {} e do cateto adjacente é {} então o comprimento da hipotenusa é {:.2f}'.format(co,ca,hip))

#18

import math
a = float(input('Digite o angulo que você deseja?'))
print('Seno:{:.2f}'.format(math.sin(math.radians(a))))
print('Cosseno:{:.2f}'.format(math.cos(math.radians(a))))
print('Tangente:{:.2f}'.format(math.tan(math.radians(a)))) 

#19

import random
nome = 'Gui','hugo','rafa','joao'
sorteio = random.choice(nome)
print(sorteio)

// 

import random
n1 = str(input('Digite o primeiro nome:'))
n2 = str(input('Digite o segundo nome:'))
n3 = str(input('Digite o terceiro nome:'))
n4 = str(input('Digite o quarto nome:'))
num = [n1,n2,n3,n4]
sorteio = random.choice(num)
print('O nome escolhido para apagar o quadro foi {}'.format(sorteio))

#20

import random
n1 = str(input('Digite o primeiro nome:'))
n2 = str(input('Digite o segundo nome:'))
n3 = str(input('Digite o terceiro nome:'))
n4 = str(input('Digite o quarto nome:'))
list = [n1,n2,n3,n4]
sorteio = random.shuffle(list) #mostra todos em formato random
print('A sequencia da apresentação será {} '.format(list))