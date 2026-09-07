print('='*15)
print('Gerador de PA')
print('='*15)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão do PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM!')

# Nesse programa pedimos pro usuário inserir o primeiro termo e depois a razão. No while diz que enquanto o cont for menor ou igual a 10, ele vai somando o termo com a razão, por exemplo se o termo for 0 e a razão 5, ele vai somando de 5 em 5 e o cont vai adicionando +1 até chegar em 10.