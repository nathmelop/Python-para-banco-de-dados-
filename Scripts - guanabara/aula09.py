frase  = curso em video 

frase.count('o')

frase.find('deo') # Quantas vezes ele encontrou 'deo', ele vai te mostrar que momento começou o 'deo'. 

frase.finf('android') # Quando a string não existe, ele te retorna como -1 

'curso' in frase # Ele vai te retornar como TRUE 

frase.replace('python','android') # Onde tiver python ele vai subtistuir por android. 

frase.upper() # Vai ficar em maiúsculas
frase.lower() # Minúsculas
frase.capitalize() # vai jogar tudo para minusculo e só o primeiro para maisculo
frase.title() # Analisar quantas palavras tem 

frase.strip() # Remove os espaços inuteis 
frase.rstrip() # Começa a tratar pela direita 
frase.lstrip() # Tira os espaço das esquerda 

# DIVISÃO 

frase.split() # Divisao entre os espaços, refez e recebe uma lista nova 

#JUNÇÃO

'-'.join(frase) # Juntar todos os elementos de frase  e colocar o - 


frase = 'Curso em video Python'
print(frase[:13])

frase = 'Curso em Video Python'
print(frase.count('o'))

frase = 'Curso em Video Python'
print(len(frase))

frase = 'Curso em Video Python'
print(frase.replace('Python','Android'))

frase = 'Curso em Video Python'
(frase.replace('Python','Android'))
print(frase)

frase = 'Curso em Video Python'
frase = (frase.replace('Python','Android'))
print(frase)

frase = 'Curso em video Python'
print(frase.split())

frase = 'Curso em video Python'
print(frase.lower().find('video'))

frase = 'Curso em video Python'
dividido = frase.split()
print(dividido[2][3])