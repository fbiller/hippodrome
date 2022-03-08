"""Outil de gestion de courses hippiques
Rendu 08/03 23h59
Hippodrome (un seul, nom),
Course (nom, date, 6 chevaux),
cheval(nom, âge, nombre de victoire).
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
import unittest
import sys
from unittest import TestCase, mock
from hypodrome import Cheval, Saisie
from io import StringIO
from unittest.mock import patch

class persistance (TestCase):
    def setUp(self):
        self._ch1_name="Yvan"
        self._ch1_age=3
        self._ch1_nb_vic=3
        self._ch2_name="Yvanovich"

    def test_ecriture_cheval (self):
        # vérifie que l'ajout d'un cheval se retrouve dans la base "chevaldb'
        Cheval(self._ch1_name,self._ch1_age,self._ch1_nb_vic).add_cheval()
        self.assertEqual(Cheval.presence_cheval(self._ch1_name),True)

    def test_presence_cheval (self):
        # Vérifie qu'un cheval se trouve dans la base
        self.assertEqual(Cheval.presence_cheval(self._ch1_name), True)

    def test_add_victory (self):
        # Vérifie que cheval_name a vu son nombre de victoire incrémenté de 1
        Cheval(self._ch1_name, self._ch1_age, self._ch1_nb_vic).add_cheval()
        Cheval.add_victory(self,self._ch1_name)
        nb_victory = Cheval.cheval_in_db(self,self._ch1_name)[1]
        self.assertEqual(nb_victory,self._ch1_nb_vic+1)

    def test_sup_cheval (self):
        # Vérifie qu'un cheval suprimé n'est plus dans la base
        # Le test test_presence_cheval doit être effectué avant
        Cheval.sup_cheval(self,self._ch1_name)
        self.assertEqual(Cheval.presence_cheval(self._ch1_name), False)


        pass

    def tearDown(self):
        pass

class Test_saisie (TestCase):
    input_age_wrong_range = "1"
    input_age_wrong_type = "L"
    input_name_wrong_size = "ID"

    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
        self.input_name_wrong_size = "ID"

    def test_saisie_nom_cheval_affichage_erreur (self):
        # Affiche bien le messge d'erreur en cas de mauvaise saisie du nom
        Saisie().verifie_saisie_cheval("UU")
        self.assertEqual(sys.stdout.getvalue().strip(),"Le nom du cheval doit comporter 5 caractères")

    @patch('builtins.input', return_value="1")
    def test_saisie_age_out_range (self,input):
        # Affiche bien le messge d'erreur en cas de mauvaise saisie de l'age <2
        Saisie().saisie_age()
        self.assertEqual(sys.stdout.getvalue().strip(),"Veuillez entrer un nombre entre 2 et 10 ans")

    @patch('builtins.input', return_value="DD")
    def test_saisie_age_string (self,input):
        # Affiche bien le messge d'erreur en cas de mauvaise saisie de l'age 'string')
        Saisie().saisie_age()
        self.assertEqual(sys.stdout.getvalue().strip(),"Veuillez entrer un nombre entre 2 et 10 ans")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

"""
    def test_saisie_nom_cheval_affichage_erreur (self):
        original_input = mock.builtins.input
        mock.builtins.input = lambda _:"ND"
        # Affichie bien le messge d'erreur en cas de mauvaise saisie du nom
        Saisie().verifie_saisie_cheval(self)
        self.assertEqual(sys.stdout.getvalue().strip(),"Le nom du cheval doit comporter 5 caractères")

    def tearDown(self):
        pass
"""

