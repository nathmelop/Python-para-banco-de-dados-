#12
preco = float(input('Qual é o preço do produto? R$'))
novo = preco - (preco * 5 / 100)
print('O produto que custava {:.2f}, na promoção com desconto de 5% vai custar R${}.'.format(preco,novo))

#13

salario = float(input('Qual o salario do funcionario? R$'))
novo = salario + (salario * 15 / 100)
print('Um funcionario que ganhava R${:.2f}, com aumento de  15% vai ganhar R${:.2f}.'.format(salario,novo))

#14 
c = float (input('informe a temperatura em C:'))
f = ((9*c)/5)+32
print('A temperatura de {}C corresponde a {}F'.format(c,f))

#15
km = float (input('Quantos km Você percorreu?'))
aluguel = int(input('Quantos dias você alugou o carro?'))
dia =  (aluguel * 60) + (km*0.15)
print('O valor a pagar é R${:.2f}'.format(dia))
