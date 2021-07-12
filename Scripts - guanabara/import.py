## import math - ele importa essas funcionalidades
Ceil - arredonda para cima 
floor -  arredonda para baixo 
trunc - Elimina da virgula para frente sem arredondar
pow - potencia 
sqrt - calcular raiz quadrada
factorial - 

de todas as funcionalidades math so quero usar a sqrt eu utilizo assim: 

- from math import sqrt  


import math
num = int(input('Digite um numero:'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num,raiz))

from math import  sqrt
num = int(input('Digite um numero:'))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num,raiz))

##usando 2 import

from math import  sqrt, floor
num = int(input('Digite um numero:'))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num,floor(raiz)))

import random
num = random.randint(1,10)
print(num)

import emoji
print(emoji.emojize("Olá mundo :neckbeard:",use_aliases=True))