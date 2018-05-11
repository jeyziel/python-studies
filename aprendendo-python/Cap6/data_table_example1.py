class DataTable():
    def __init__(self, name):
        self._name = name
        self._collumn = []
        self._data = []
    
    def get_name(self):
        return self._name
    
    @property
    def data(self):
        return self._data

class Column():
    def __init__(self, name, kind, description):
        self._name = name
        self._kind = kind
        self._description = description


table = DataTable('venda')

print(table.data)
print(table.get_name())