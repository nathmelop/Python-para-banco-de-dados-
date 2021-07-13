# Crie um programa que leia o nome completo de uma pessoa e mostre: 

# - O nome com todas as letras maiúsculas
nome = str(input('Digite seu nome completo:'))
print(nome.upper()) 

# - O nome com todas minusculas
nome = str(input('Digite seu nome completo:'))
print(nome.lower())

# - Quantas letras ao todo (sem considerar espaços)
nome = str(input('Digite seu nome completo:')).strip()
print(len(nome)-nome.count(' '))

#  - Quantas letras tem o primeiro nome 
nome = str(input('Digite seu nome completo:')).strip()
contando = nome.split()
print(len(contando[0]))
