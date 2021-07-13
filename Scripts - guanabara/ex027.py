# Faça um programa que leia o nome completo de uma pessoa, mostrandoem seguida o primeiro e o ultimo nome separadamente. 

nome = str(input('Digite seu nome completo:')).strip()
divide = nome.split()
print('Primeiro: {}'.format(divide[0]))
print('Ultimo: {}'.format(divide[len(divide)-1]))