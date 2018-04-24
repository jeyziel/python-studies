from twp352_banco_tatu import Cliente
from twp352_banco_tatu import Conta

joao = Cliente('joao da silva', '777-555')
maria = Cliente('maira da silva', '555-777')

conta1 = Conta(joao, 155, 100)
conta2 = Conta([joao, maria], 255, 50)

conta1.resumo()
conta2.resumo()