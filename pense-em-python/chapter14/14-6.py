import dbm

db = dbm.open('captions', 'c')

db['cleese.png'] = 'Photo of jhon cleese'

print(db['cleese.png'])


for key in db:
    print(key, db[key])

db.close()
