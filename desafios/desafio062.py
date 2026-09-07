print('='*15)
print('Gerador de PA')
print('='*15)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão do PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? (Para encerrar digite 0): '))
print('Progressão finalizada com {} termos mostrados.'.format(total))

# Nesse programa pedimos pro usuário inserir o primeiro termo e depois a razão. No primeiro while dizemos que enquanto a variável mais for diferente de 0, a variavel total recebe valor 10 e se inicia o segundo while que enquanto cont for menor ou igual a total(10), ele vai somando o termo com a razão, por exemplo se o termo for 0 e a razão 5, ele vai somando de 5 em 5 e o cont vai adicionando +1 até chegar em 10. Depois ele pergunta quantos termos o usuário quer que mostre. Quando o usuário digitar 0, o programa se encerra e diz quantos termos foram mostrados.