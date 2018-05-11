

class Relationship():
    """Classe que representa um relacionamento entre DataTables.
    Essa classe tem todas as informações que identificam um
    relacionamento entre tabelas. Em qual coluna ele existe,
    de onde vem e pra onde vai.
    """
    def __init__(self, name, _from, to, on):
        self._name = name
        self._from = _from
        self._to = to
        self._on = on


class DataTable():
    
    def __init__(self, name):
        self._name = name
        self._collumns = []
        self._references = []
        self._referenced = []
        self._data = []
    
    def add_column(self, name, kind, description = ""):
        column = Column(name, kind, description)
        self._collumns.append(column)
        return column
    
    def add_references(self, name, to, on):
        """Cria uma referencia dessa tabela para uma outra tabela
        Args:
        name: nome da relação
        to: instância da tabela apontada
        on: instância coluna em que existe a relação
        """
        relationship = Relationship(name, self, to, on)
        self._references.append(relationship)

    def add_referenced(self, name, by, on):
        """Cria uma referência para outra tabela que aponta para
        essa.
        Args:
        name: nome da relação
        by: instância da tabela que aponta para essa
        on: instância coluna em que existe a relação
        """
        relationship = Relationship(name, by, self, on)
        self._referenced.append(relationship)

class Column():
    def __init__(self, name, kind, description):
        self._name = name
        self._kind = kind
        self._description = description

##próximo capitulo = 6.6