

eng2sp = dict()

eng2sp['one'] = 'uno'
eng2sp['two2'] = 'dos'

print(eng2sp)

if 'one' in eng2sp:
    print('encontrado')

##nao será encontrado, pois, aparecer como valor não é suficiente
if 'uno' in eng2sp:
    print('encontrado')

if 'uno' in eng2sp.values():
    print('encontrado')
