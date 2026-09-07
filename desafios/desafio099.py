def maior(*núm):
    print('-='* 20)
    print('Analisando os valores passados...')
    print(f'{núm} Foram informados {len(núm)} valores ao todo.')
    print(f'O maior valor informado foi {max(núm)}.')

maior(2, 4, 7, 55, 9)
maior(3, 45, 100, 1)
maior(2, 3)
maior(1)