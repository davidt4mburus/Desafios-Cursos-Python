import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://fisioterapeuta-lucas-tamburus.netlify.app/')
except Exception as e:
    print(e)
    print('O site não está acessível no momento.')
else:
    print('O site está funcionando.')