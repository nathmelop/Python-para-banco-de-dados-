km = int(input('Quantos km você estava?'))
multa = (km - 80)*7
print('Sua velocidade foi {}'.format(km))
if km >= 80:
    print('Você foi multado, o valor da multa é R$ {} reais'.format(multa))