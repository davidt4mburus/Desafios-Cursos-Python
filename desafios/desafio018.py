import math
ang = int(input('Digite o valor do ângulo: '))
ang_rad = math.radians(ang)
seno = math.sin(ang_rad)
cosseno = math.cos(ang_rad)
tangente = math.tan(ang_rad)
print('O valor do seno é {}, cosseno {} e tangente {}'.format(seno, cosseno, tangente))