# Leia um programa que leia uma frase pelo teclado e mostre:

nome = str(input('Digite um nome:')).strip()
print('Quantas vezes a letra A aparece: {}'.format(nome.count('a')))
print('Em que posição ela aparece a primeira vez: {}'.format(nome.find('a')))
print('Em que posição ela aparece a ultima vez: {}'.format(nome.rfind('a')))