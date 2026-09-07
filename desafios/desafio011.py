l = float(input('Qual a largura da parede em metros: '))
a = float(input('Qual a altura da parede em metros: '))
at = a * l
tinta = at / 2
print('A área total é: {:.2f} m²'.format(at))
print('Será necessário {:.2f} de tinta'.format(tinta))