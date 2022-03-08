
"""Outil de gestion de courses hippiques
Rendu 08/03 23h59
Hippodrome (un seul, nom), Course (nom, date, 6 chevaux), cheval(nom, âge, nombre de victoire).
Indépendant les uns des autres.
Menu en console.
CRUD sur course et cheval.
R sur Hippodrome (resultats) -> lister les 10 dernières courses et le cheval qui a gagné.
Outil qui génère les résultats de course.
Enregistrement des données (bdd, fichier txt)

Travail en binôme. Les noms des membres du binôme seront indiqué dans un readme.
Le code sur github, et le lien sera rendu sur Moodle.
Le taux de couverture doit être de 75% minimum.
Chaque test doit passer.
Un fichier readme expliquera succinctement la stratégie de tests."""
import shelve
import random

class hypo:
    def __init__(self):
        pass

class Course:
    def __init__ (self,input_name,input_date):
        self.name = input_name
        self.date = input_date
        self.list_chevaux = []
        self.gagnant = input_gagnant

    def ajoute_course (self):
        #ajoute une course en base
        db= shelve.open("coursedb")
        db[self.name] = Cheval(self.name, self.date, self.list_chevaux)
        db.close()

    def affiche_course (self):
        """ retourne la composition d'une course"""
        statemnt = 'La course ' + self.name + " du " + self.date + " a les chevaux suivants "
        print (statemnt)
        for cheval in self.list_chevaux :
            print (cheval)

    def ajoute_cheval (self,course_name):
        db = shelve.open ("coursedb")
        data_course = db[course_name]
        data_course.list_chevaux = data_course.list_chevaux.append(Cheval.choix_nom())
        db[course_name] = data_course
        db.close()

    def __exit__(self):
        db.close()


pass

class Saisie:
    def __init__(self):
        pass

    def saisie_cheval (self):
        cheval_name = input('Entrez le nom du Cheval ')
        if Saisie().verifie_saisie_cheval (cheval_name):
            Saisie().saisie_cheval()
        return saisie_cheval

    def verifie_saisie_cheval (self,cheval_name):
        if len (cheval_name) <= 4:
            print("Le nom du cheval doit comporter 5 caractères")
            return True

    def saisie_age (self):
        age_cheval = input('Age du Cheval ')
        if Saisie().verifie_saisie_age(age_cheval):
            print("Veuillez entrer un nombre entre 2 et 10 ans")
            #Saisie().saisie_age()
        return age_cheval

    def verifie_saisie_age (self,age_cheval):
        try:
            if int(age_cheval) in range (2,11):
                return False
        except ValueError:
            return True
        else:
            return True

class Cheval:
    def __init__ (self,name=None,age=None,nb_vic=None):
        self.name = name
        self.age = age
        self.nb_vic=nb_vic

    def choix_nom(self):
        """retourne un élément tiré au hasard de la liste noms_insolite"""
        noms_insolite = ['Rabbi Jacob', 'Poltergeist', 'Marathon Man', 'Silence On Tourne',
                         'La Patate', 'L’Osso Bucco', 'Nem', 'Ta Chouchoute', 'Tarte aux Fraises',
                         'Épinard', 'Litchi', 'Maldini', 'Inzaghi', 'Tête de Zizou',
                         'Tatayoyo', 'Cœur de Rocker', 'Pas Peur de Toi', 'Tape à l’œil', 'Pas de Blabla',
                         'Bien Costaud', 'Yapaphoto', 'Maxibon', 'Maldini', 'Inzaghi', 'Tête de Zizou'
                         'Lamentable', 'Non Partant',
                         'N’y Touchez Pas', 'Poilu de France',
                         'Nabuchodonosor', 'Rien Ne Va Plus', 'Atchoum', 'Crack Boum Wizz',
                         'On Vient de Bouère', 'Kilo de Trot', 'Mélagom', 'Mapoolish',
                         'Encombremenminimum', 'Nuit Torride', 'Le Petit Kiki', 'La Turlutte']
        return random.choice(noms_insolite)

    def Af_description(self):
        """ retourne les nom age et nombre de victoire d'un cheval"""
        statemnt = self.name,self.age,self.nb_vic
        return statemnt

    def description (self):
        "retourne les nom age et nombre de victoire d'un cheval"""
        statemnt ='Le cheval '+ self.name + " a " + str(self.age) + " ans et remporté " \
                  + str(self.nb_vic) + " victoire(s)"
        return statemnt

    def sup_cheval(self,cheval_name):
        #Supprime cheval_name en base
        db = shelve.open('chevaldb')
        if Cheval.presence_cheval(cheval_name):
           del db[cheval_name]

    def add_cheval(self):
        #ajoute un cheval en base
        db = shelve.open('chevaldb')
        db[self.name] = Cheval (self.name,self.age,self.nb_vic)
        db.close()

    def add_victory(self,cheval_name):
        """" ajoute une victoire au cheval_name"""
        db = shelve.open('chevaldb')
        ch1 = db[cheval_name]
        ch1.nb_vic +=1
        db[cheval_name]=ch1
        db.close()

    def presence_cheval(cheval_name):
        # Vérifie si un cheval est présent en base"
        db = shelve.open('chevaldb')
        index = db.keys()
        return cheval_name in index

    def chevaux_in_db_affiche (self,clef=""):
        """" affiche les chevaux présents dans la bdd cheval
        avec leur age et nombre de victoire"""
        db = shelve.open('chevaldb')
        if clef=="" :
            for obj in db.keys():
                print(db[obj].description())
            exit()
        else:
            #print(db[clef].description())
            print ("else")

    def cheval_in_db (self,clef):
        """" retourne l'age et le nombre de victoire d'un cheval présent en
        base"""
        db = shelve.open('chevaldb')
        index = db.keys()
        if clef in index :
            data_cheval = db[clef]
            return(data_cheval.age, data_cheval.nb_vic)
        else:
            return False

    def __exit__(self):
        db.close()


#print (Cheval ("Yvanovich",5,3).description())
#
#Cheval().sup_cheval("Yvanovich")
#Cheval().chevaux_in_db_affiche("")
#ch=Cheval().cheval_in_db("Yvanovich")[0]

#Cheval.ajoute_course("id1",["Course 1","24/01/22","Ch1","Ch2","Ch3","Ch4","Ch5","Ch6"])
#ChevalDict = {}
#Cheval.ajoute_cheval("ch1",['Yvanovich',5,3])
#Cheval.ajoute_cheval("ch2",['Yvah',3,2])
#print(ChevalDict)

Cheval (Cheval().choix_nom(),5,3).add_cheval()
Cheval().chevaux_in_db_affiche("")

Course("Course1","date1").ajoute_course()
