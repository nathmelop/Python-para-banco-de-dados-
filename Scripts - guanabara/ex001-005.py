nome = input ('Digite seu nome:')
print('É um prazer te conhecer',nome,'!')

print('Olá, Mundo')

nome = input ('Digite seu nome:')
print('É um prazer te conhecer, {}!'.format(nome)) #colocando nome dentro do {} usando format 

#03 
 n1 = int(input('digite um valor:'))
n2 = int(input('digite outro valor:'))
s = n1 + n2
print('A soma entre {} e {} é igual a {}'.format(n1,n2,s))

#4

algo =input('digite algo:')
print('O tipo primitivo desse valor é',type(algo))
print ('Só tem espaços:', algo.isspace())
print('É um numero?', algo.isnumeric())
print('É alfabetico?', algo.isalpha())
print('é alfanumérico?',algo.isalnum())
print('está em maiúscula?', algo.isupper())
print('está em minuscula?', algo.islower())
print('está capitalizada?', algo.istitle())