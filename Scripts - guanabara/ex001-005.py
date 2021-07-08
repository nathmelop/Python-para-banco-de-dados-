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

#05
n1 = int(input('Digite um numero:'))
n2 = n1 + 1
n3 = n1 - 1
print('O numero digitado é {} e seu sucessor é {} e seu antecessor é {}!!'.format(n1,n2,n3))

#6 
n1 = int(input('digite um valor:'))
m = n1 * 2
t = n1 *3
e = n1 ** (1/2)
print('O numero é {} o dobro é {} \n o triplo é: {} \n é a raiz quadrada é:{:.2f}'.format(n1,m,t,e))
 //

 n = int(input('digite um valor:'))
 print('O numero é {} o dobro é {}  o triplo é: {} é a raiz quadrada é:{}'.format(n*2,n*3,n1**2))

 #7
 n1 = float(input('Primeira nota do aluno:'))
n2 = float(input('Primeira nota do aluno:'))
m = (n1 + n2) / 2
print('A média entre {} e {}  é igual há : {}'.format(n1,n2,m))

#8 
n = float(input('Digite um numero em metros:'))
k = n / 1000
h = n / 100
d = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000
print('A medida de {} corresponde  a \n {}km \n {}hm \n {}dam \n {}dm \n {}cm \n {}mm'.format(n,k,h,d,dm,cm,mm))

#9 

n = int(input('Digite um numero para visualizar sua tabuada:'))
n1 = n * 1
n2 = n * 2
n3 = n * 3
n4 = n * 4
n5 = n * 5
n6 = n * 6
n7 = n * 7
n8 = n * 8
n9 = n * 9
n10 = n * 10
print('{} X 1 = {}'.format(n,n1))
print('{} X 2 = {}'.format(n,n2))
print('{} X 3 = {}'.format(n,n3))
print('{} x 4 = {}'.format(n,n4))
print('{} X 5 = {}'.format(n,n5))
print('{} X 6 = {}'.format(n,n6))
print('{} X 7 = {}'.format(n,n7))
print('{} X 8 = {}'.format(n,n8))
print('{} X 9 = {}'.format(n,n9))
print('{} X 10 = {}'.format(n,n10))

#10

n = float(input('Transformador de dolar para real:'))
print('US{} Equivale a R${:.2f} .'.format(n,3.27 * n))

#11

largura =float(input('Qual a largura da sua parede?'))
altura =float(input('Qual a altura da sua parede?'))
area = largura * altura
print ('Sua parede tem a dimensao de {}X{} e sua área é de {}m.'.format(largura,altura,area))