import shelve

db= shelve.open ('chevaldb')

print(len(db))
print(list(db.keys()))

ch1 = db['Ideal du gazon']
ch1.nb_vic +=1
db['Ideal du gazon']=ch1

print(db['Ideal du gazon'].description())
db.close()