"""
POO - Métodos
- Métodos (funções)-> Representam os comportamentos dos objetos. Ou seja, as ações que este objeto
pode realizar no seu sistema.

Em Python, dividimos nossos métodos em dois grupos: Métodos de Instâncias e Métodos de Classe.
Quando uma função está contida dentro de uma classe, ela é chamada de método.

Obs: O método dunder init (__init__), é um método especial chamado de construtor e sua função é
construir o objeto a partir da classe.

Obs: Para utilizar Métodos de Classe, utiliza-se a palavra reservada @classmethod

Obs: Métodos de instância utilizam atributos de instâncias, e métodos de classe, utilizam atributos
de classe. Por isso, quando se utiliza um método que não usa atributos de instância, é sujerido
criado como método de classe (@classemethod)

Obs: Métodos de Classe em outras linguagens são conhecidos como métodos estáticos (java, C, C++)

Obs: Assim como é possível criar atributos privados usando duplo underline (__dunder), também é possivel
criar métodos privados, também utilizano-se o duplo underline.

Obs: Também é possível criar métodos estáticos que não utilizam atributos de classe nem atributos de instancias,
para isso, utiliza-se a palavra reservada @staticmethod, como no exemplo da classe Lampada.
"""

# Métodos de Instâncias


class Lampada:

    @staticmethod
    def definicao():
        return 'Testando o metodo estatico'

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def __privado(self):
        return self.__cor.title()


class ContaCorrente:

    contador = 0000

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return f'A compra do {self.__nome}, ' \
               f'com desconto de {porcentagem}%, ' \
               f'será: R$ {self.__valor * (100 - porcentagem) / 100}'


from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0

    @classmethod
    def conta_usuario(cls):
        print(f'Temos {cls.contador} usuário(s) no sistema')

    @classmethod
    def ver(cls):
        print('Testando o metodo de classe')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


# -----------------------------------------------------------------------------------------------
# Instanciando produtos e aplicando descontos
prod1 = Produto('PlayStation', 'Video Game', 1565)
prod2 = Produto('Notebook', 'Computador', 4000)
print(prod1.desconto(20))
print(prod2.desconto(15))

print(Produto.desconto(prod1, 10))
print(Produto.desconto(prod1, 50))
print(Produto.desconto(prod2, 70))
print(Produto.desconto(prod2, 40))
print(30 * '-+-')

# -----------------------------------------------------------------------------------------------
# Instanciando Usuários (nome, sobrenome, email, senha)

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
email = input('Digite seu melhor email: ')
senha = input('Digite sua senha: ')
confirma_senha = input('Confirme a senha: ')
print(30 * '-+-')

if senha == confirma_senha:
    user1 = Usuario(nome, sobrenome, email, senha)

else:
    print('Senha incorreta')
    exit(1)

print('Usuario criado com sucesso!')

senha = input('Informe a senha para acesso: ')

if user1.checa_senha(senha):
    print('Acesso permitido\n')
    print(f'Seja bem vindo, {user1.nome_completo().title()}\n')
else:
    print('Acesso negado\n')

#print(f'Senha encryptografada: {user1._Usuario__senha}') # Acesso errado

# Utilizando metodos de classes
Usuario.conta_usuario()
Usuario.ver()

# -----------------------------------------------------------------------------------------------
# Instanciando a classe Lampada (cor, voltage, luminosidade)
lamp1 = Lampada('vermelha', 120, 'alta')

print(lamp1.definicao())
print(lamp1._Lampada__privado)
