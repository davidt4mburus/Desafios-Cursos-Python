from hashlib import sha256
from rich import print

class Credencial():
    def __init__(self):
        self.__hash = None

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, chave):
        if len(chave) > 0:
            self.__hash = sha256(chave.encode('utf-8')).hexdigest()
        else:
            raise ValueError('Senha Inválida!')

    def validar(self, chave):
        usuario = sha256(chave.encode('utf-8')).hexdigest()
        if usuario == self.__hash:
            print(f'[green]ACESSO LIBERADO![/]')
            return True
        else:
            print(f'[red]ACESSO NEGADO! SENHA INVÁLIDA.[/]')
            return False

""" EXPLICANDO HASH

from hashlib import sha256 # Importar biblioteca hash para codificação.

# SHA = Secure Hash Algorithm
texto = 'Gafanhoto'
cod = texto.encode('utf-8') # utf-8 mais utilizado no EUA e BR
hash = sha256(cod).hexdigest() # Codificando a senha em hex.

print(hash) """