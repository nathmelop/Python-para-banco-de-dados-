# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome de uma cidade:')).strip()
print('Caso ela comece com Santo ela retorna um valor: {}'.format(cidade[:5].upper() == 'SANTO'))

# Resolução do vitor 

cidade = str(input('Digite o nome da cidade: ')).strip()
print('O nome dessa cidade começa com Santo: {}'.format(cidade[:5].upper() == 'SANTO'))