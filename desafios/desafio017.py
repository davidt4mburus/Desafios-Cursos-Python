import math
cat_oposto = int(input('Digite o valor do cateto oposto: '))
cat_adj = int(input('Digite o valor do cateto adjacente: '))
hip = math.hypot(cat_adj, cat_oposto)
print('O resultado da hipotenusa é {}'.format(hip))