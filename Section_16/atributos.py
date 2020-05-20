"""
POO - Atributos
Atributos representam as caracteristicas dos objetos, pelos atributos, conseguimos representar computacionalmente
os estados de um objeto

Em Python, dividimos os atributos em 3 grupos:
    -Atributos de instâncias;
    -Atributos de Classes;
    -Atributos Dinâmicos;

Atributos de instâncias são atributos declarados dentro do método Construtor
Método Construtor é um método especial utilizado para a construção de objetos

Obs: Em python, ficou estabelecido que todo atributo de uma classe é público, ou seja
pode ser acessado em todo projeto. Caso queiramos deonstrar que determinado atributo deve
ser tratado como privado, ou seja, que deve ser acessado/utilizado somente dentro da própria
classe onde está declarado, utiliza-se __ duplo underscore no inicio do seu nome.
Isso é conhecido também como Name Mangling.

Obs: Em linguagem como JAVA, atributos de Classe são chamados de atributos estáticos

Obs: Atributos Dinâmicos são atributos de instâncias que podem ser criados em tempo de
execução. O atributo dinâmico será exclusivo da instância que o criou.
"""

# Atributos de Instâncias (Públicos)


class Lampada:

    def __init__(self, voltagem, cor):
        self.cor = cor
        self.voltagem = voltagem
        self.ligada = False


class ContaCorrente:

    def __init__(self, nome, limite, saldo):
        self.saldo = saldo
        self.limite = limite
        self.nome = nome


class Produto:

    # Atributo de classe
    imposto = 1.05 # 0.05% de imposto
    id = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.id + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.id = self.id





class Usuario:

    def __init__(self, nome, email, senha):
        self.senha = senha
        self.email = email
        self.nome = nome

# A tributos públicos e privados


class Acesso:

    def __init__(self, nome, email, senha):
        self.__senha = senha
        self.__nome = nome
        self.__email = email

    def mostra_nome(self):
        print(self.__nome)

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.__email)


user1 = Usuario('Olímpio Barbosa dos Santos Junior', 'olimpio@gmail.com', 1234)
print(user1.email)
print(user1.nome)
print(user1.senha)

# Retorna AtributeError
user2 = Acesso('Olimpio Júnior', 'olimpio@outlook.com', 99810154)
# print(user2.__nome)
# print(user2.__email)

print(dir(user2))

# Acessando atributos privados (Name Mangling) - não usual
print(user2._Acesso__email)
print(user2._Acesso__nome)
print(user2._Acesso__senha)
print(30 * '--')

# Acessando atributos privado forma correta
user2.mostra_senha()
user2.mostra_email()
print(30 * '--')

# Inserindo Atributos
user0001 = Acesso('Pedro', 'pedro@geek.com', 1256)
user0002 = Acesso('Miguel', 'miguel@geek.com', 3467)
user0003 = Acesso('Raquel', 'raquel@geek.com', 3456)

# Dados do primeiro usuário
user0001.mostra_nome()
user0001.mostra_email()
user0001.mostra_senha()

# Dados do segundo usuário
user0002.mostra_nome()
user0002.mostra_email()
user0002.mostra_senha()

# Dados do terceiro usuário
print('Nome, Email, Senha')
user0003.mostra_nome()
user0003.mostra_email()
user0003.mostra_senha()

print(30 * '--')

for usuario in user0001, user0002, user0003:
    print(usuario.__dict__)
    usuario.mostra_senha()
    usuario.mostra_nome()
    usuario.mostra_email()
    print(20 * '--')

# Atributos de Classes para Classe Produto
prod001 = Produto('PlayStation', 'Video game', 2300)
prod002 = Produto('Notebook', 'Computador', 4000)

print(f'O valor do Produto 1 será: {prod001.valor}')
print(f'O valor do Produto 2 será: {prod002.valor}')
print(f'Valor de imposto: {Produto.imposto}')

print(f'Id: {prod001.id}')
print(f'Id: {prod002.id}')
print(30 * '--')

# Atributo Dinâmicos - Não usual
prod001.peso = '2Kg' # Note que na classe Produto não existe o atrbuto peso.

print(f'Produto: {prod001.nome}\n'
      f'Descrição: {prod001.descricao}\n'
      f'Valor: {prod001.valor}\n'
      f'Peso: {prod001.peso}')

# Deletando atributos
print(20 * '-_-_')
print(prod001.__dict__)
print(prod002.__dict__)

del prod001.peso

print(20 * '-_-_')
print(prod001.__dict__)
print(prod002.__dict__)