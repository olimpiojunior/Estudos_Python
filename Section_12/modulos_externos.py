''''
Utilizando o gerenciador de pacotes python chamado Pip

from colorama import init, Fore, Back

#utilizando pacote colorama instalado com pip install colorama
init()
print(Fore.MAGENTA + 'Olimpio barbosa')
print(Fore.LIGHTBLUE_EX + 'Olimpio barbosa')
print(Fore.BLACK + 'Olimpio barbosa')
print(Fore.GREEN + 'Olimpio barbosa')
print(Fore.RED + 'Olimpio barbosa')

#nome com fundo colorido
print(Back.GREEN + 'Olimpio Barbosa')
print(Back.BLUE + 'Olimpio Barbosa')
print(Back.LIGHTMAGENTA_EX + 'Olimpio Barbosa')
print(Back.WHITE + 'Olimpio Barbosa')
'''
#manipulando pdf com python-pdf
import pydf
pdf = pydf.generate_pdf('<h1>Olimpio Junior</h1><br/><br/><strong>Trabalhando com pdf em Python</strong>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
