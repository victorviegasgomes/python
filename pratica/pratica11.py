print('considere que um balde de tinta consiga pintar 2m²')
height = int(input('digite a altura de uma parede: '))
width = int(input('agora digite a largura: '))
area = width * height
print('a área da parede é: {}'.format(area))
print('você precisa de {} baldes de tinta para pintar a parede'.format(area/2**2))
