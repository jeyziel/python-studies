from twp353_tatu2 import Cliente
from twp353_tatu2 import Conta
from twp353_tatu2 import ContaEspecial

maria = Cliente('maria da silva', '755-455')
joao = Cliente('joao da silva', '123-456')
jose = Cliente('jose da silva', '123-456')

conta1 = Conta(joao, '155', 2000)
conta2 = Conta([joao, maria], '255', 1000)
conta_especial = ContaEspecial(jose, '2', 5000, 1000)


conta1.deposito(1000)
conta1.saque(500)

conta2.deposito(2000)
conta2.saque(700)

conta_especial.saque(5500)

conta1.extrato()
conta2.extrato()
conta_especial.extrato()
