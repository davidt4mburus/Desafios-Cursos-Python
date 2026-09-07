primeiro = int(input('Digite primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range (primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' → ')
print('Acabou!')