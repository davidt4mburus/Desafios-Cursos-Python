from classes032 import *

def main():
    cc = ContaBancaria(id=111, nome='David', saldo=10_000)
    
    print('Realizar saque...')
    cc.sacar(500)

    print('Trocar nome titular...')
    cc.nome = 'Maricota'

    print(cc)
    
if __name__ == '__main__':
    main()