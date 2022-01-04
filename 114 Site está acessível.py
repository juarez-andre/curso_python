import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mNão foi possível acessar o site.\033[m')
else:
    print('\033[32mO site está acessível.\033[m')
    print(site.read())