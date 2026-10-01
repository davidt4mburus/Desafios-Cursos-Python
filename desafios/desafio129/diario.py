from rich import print

class Diario:
    def __init__(self, senhamestra='ABC'):
        self.__segredos = []
        self.__senha = senhamestra


    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0: # Se a mensagem de instancia for string e a quantidade de letras da mensagem for maior que 0
            self.__segredos.append(msg.strip())


    def ler(self, senha= None):
        if senha != self.__senha:
            raise PermissionError('Senha inválida! Você não pode ler meu diário!')
        else:
            print('[green]DIÁRIO LIBERADO[/]')
            for segredo in self.__segredos:
                print(f'- {segredo}')


    @property
    def senha(self):
        raise PermissionError(f'Ninguém tem permissão de ver a senha.')