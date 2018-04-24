import datetime

class Pessoa():
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.nascimento = data_nascimento

    def idade(self):
        delta = datetime.date.today() - self.nascimento
        return int(delta.days/365)

    def __str__( self ):
        return '%s tem %d anos' %(self.nome, self.idade())

jeyziel = Pessoa('jeyziel', datetime.date(1999,1,21))

print(jeyziel.idade())
print(jeyziel)