from hypodrome import Cheval
import shelve

ch1 = Cheval(name="Ideal du gazon",age=5,nb_vic=15)
ch2 = Cheval(name="Henri IV",age=3,nb_vic=6)

db= shelve.open ('chevaldb')

for obj in (ch1,ch2):
    db[obj.name]=obj

db.close()

