import os

meta = {
    'instituicao': [
        ('IdInstituicao', 'bigint', 'Identificador da instituição-PK'),
        ('IdTipoInstituicao', 'bigint',
        'Id do tipo de instituição'),
        ('NomInstituicao', 'varchar', 'Nome da instituição'),
        ('NumCnpj', 'varchar', 'Número do CNPJ')
    ]
}

# for meta_file in os.listdir('data/meta-data'):
#     print(meta_file)

def extract_entity_name(filename):
    return filename.split('.')[0]

def read_lines(filename):
    _file = open(os.path.join("data/meta-data", filename), "rt")
    data = _file.read().split('\n')
    _file.close()
    return data

def read_meta_data(path):
    meta_data = []
    for column in read_lines(path):
        if column:
            values = column.split('\t')
            nome = values[0]
            tipo = values[1]
            desc = values[2]
            meta_data.append((nome, tipo, desc))
    return meta_data

def prompt():
    print("\nO que deseja ver?")
    print("(l) Listar entidades")
    print("(d) Exibir atributos de uma entidade")
    print("(r) Exibir referências de uma entidade")
    print("(s) Sair do programa")
    return input('')

def main():
    meta = {}

    keys = {}

    relationships = {}

    for meta_data_file in os.listdir("data/meta-data"):
        table_name = extract_entity_name(meta_data_file)
        attributes = read_meta_data(meta_data_file)
        identifier = attributes[0][0]

        meta[table_name] = attributes
        keys[identifier] = table_name ## keys['idempre] = empreedimento 
    # print(keys)
    # print()
    

    for key, val in meta.items():
        #key = entidade
        #val = colunas
        for col in val:
            if col[0] in keys:
                if not col[0] == meta[key][0][0]:
                    relationships[key] = keys[col[0]]
                    #print("Entidade {} -> {}".format(key, col[0]))

    opcao = prompt()


    while opcao != 's':
        if opcao == 'l':
            for entity_name in meta.keys():
                print(entity_name)
        elif opcao == 'd':
            entity_name = input('Nome da entidade: ')
            for col in meta[entity_name]:
                print(col)                   
        elif opcao == 'r':
            print(relationships)
            print()
            print()
            entity_name = input('Nome da entidade: ')
            other_entity = relationships[entity_name]
            print(other_entity)
        else:
            print('Inexistente \n')
        opcao = prompt()

main()

# print(read_meta_data('Instituicao.txt'))

# print(os.path.join("data/meta-data", 'Instituicao.txt'))
