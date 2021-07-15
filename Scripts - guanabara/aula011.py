# Cor em python 
# \033[style;text;background;m

 print('\033[7;33;44m olá mundo\033[m')

a = 3
b = 5
print('Os valores são \033[32m{}\33[m e \33[31m{}\33[m !!!'.format(a,b))

nome = 'nathalia'
print('Olá, Prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m',nome,'\033[m'))

nome = 'nathalia'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá, Prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'],nome,cores['limpa']))


