cars = {}

cars['corola'] = 'red'
cars['fusca'] = 'blue'
cars['fit'] = 'black'

print(cars)


people = dict(jeyziel='son', maria = 'mother', jose = 'father')

if 'jeyziel' in people:
    print(people['jeyziel'])

print(people)

family = {
    'sister' : 'adna',
    'father' : 'jose',
    'mother' : 'maria',
    'grandmother' : {
        'maria Neuza', 'gertrudez'
    }

}

print(family['grandmother'])

# 
# ITERANDO DICIONARIO
# 

print("iterando dicionario")

for key, value in cars.items():
    print(key + " " + value)
