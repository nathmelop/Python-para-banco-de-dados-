# Condição
if carro.esquerda():
        bloco True 
    else:
        bloco False


tempo = int(input('Quanto anos tem seu carro?'))
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
    print('--FIM--')

    tempo = int(input('Quanto anos tem seu carro?'))
print('carro novo'if tempo <=3 else 'carro velho')
print('--fim--')

nome = str(input('Qual é o seu nome?'))
if nome == 'gustavo':
    print('Que nome lindo voce tem')
else:
    print('Que nome normal!!')
print('Bom dia!! {}'.format(nome))


n1 = float(input('digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2)/2
print('A sua media foi {:.1f}'.format(m))
if m >= 6:
    print('sua media foi boa, Parabéns!!')
else:
    print('Sua média foi ruim!! ESTUDE MAIS!!')