n = s = c = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'A soma dos {c} valores é {s}!')

# Nesse programa enquanto while for verdadeiro, pedimos pro usuário digitar um valor. Se o valor for identico a 999, o while se encerra com o break. Acaso seja diferente de 999, é realizado +1 na variavel c e n é somado na variavel s. No final é apresentado a quantidade e a soma.