def notas(* num, sit=False):
    d = dict()
    d['total'] = len(num)
    d['maior'] = max(num)
    d['menor'] = min(num)
    d['média'] = sum(num) / d['total']
    if sit:
        if d['média'] < 5:
            d['situação'] = 'Ruim'
        elif 5 <= d['média'] < 6.9:
            d['situação'] = 'Razoável'
        else:
            d['situação'] = 'Boa'
    return d

resp = notas(5.5, 1.5, 1, 6.5, sit=True)
print(resp)