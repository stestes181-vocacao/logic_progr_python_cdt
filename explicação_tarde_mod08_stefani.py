'''
Programação Orientada a objetos (POO)

Encapsulamento:

Herança:

Polimorfismo
............................................................................
class Carro:

    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor

    def buzinar (self):
        print(f'0 {self.marca} da cor {self.cor} fez Bip Bip!')

meu_carro('toyota', 'cinza')

carro_do-cliente = Carro('honda', 'preto')

meu_carro.buzinar()

carro_do_cliente.buzinar()

EXERCICIO PRÁTICO: SIMULE UM CARREGAMENTO DE BATERIA DE UM SMARTFONE, QUANDO ESTIVER
A 5%. MENSAGEM, QUANDO ESTIVER 85% AVISE QUE ESTÁ CARREGANDO.
'''
class Celular:
    def __init__(self, marca, modelo,):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False
        self.bateria = 100

    def ligar(self):
        self.ligado = True
        print(f'{self.modelo} está ligado.')

    def carregar(self):
        self.bateria = 100
        print(f'{self.modelo} está carregando. ')

meu_celular = Celular('Apple', 'iphone 16' )
meu_celular.ligar()
meu_celular.bateria = 5
print(f'{meu_celular.modelo} está com {meu_celular.bateria}% de bateria.')

