"""
class Personne:
    def __init__(self, nom, prenom, age):
        print("constructeur personne")
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age

class Etudiant(Personne):
    def __init__(self, nom, prenom, age, numeroDa):
        print("constructeur etudiant")
        self.__numeroDa = numeroDa
        super().__init__(nom, prenom, age)



#TODO une note à soi meme

#fonction mro, ordre héritage
class Humain:
    def methode(self):
        print("humain")

class Mere(Humain):
    pass

class Pere(Humain):
    def methode(self):
        print("pere")

class Bebe(Mere, Pere):
    pass

bebe= Bebe()
bebe.methode()
print(Bebe.mro())


class Appareil:
    def __init__(self, nom, couleur, annee):
        self._nom = nom
        self._couleur = couleur
        self._annee = annee

    def bruit(self):
        print("***fax machine noise***")

class Ordinateur(Appareil):
    def __init__(self, type, nom, couleur, annee):
        super().__init__(nom, couleur, annee)
        self._type = type

    def bruit(self):
        print("bagpipes")


pc = Ordinateur("linux", "henri le pc", "noir", 2006)
pc.bruit() #ce sera bagpipes
print(pc._annee) #c'est une erreur (lignes jaunes)
"""

import random
class Instruments_cordes:
    def __init__(self, nb_cordes, genre, marque):
        self._nbcordes = nb_cordes
        self._genre = genre
        self._marque = marque

    def info(self):
        print(self._nbcordes, self._genre, self._marque)

    def level(self):
        print("Your level of expertise is:")
        y = random.choice(["good", "bad", "incredible", "poser", "loser", "rockstar"])
        print(y)


class Guitare(Instruments_cordes):
    def __init__(self, nb_cordes, genre, marque, age, band):
        #age et band propre à guitare
        super().__init__(nb_cordes, genre, marque)
        self._age = age

    def reinfo(self):
        print(self._nbcordes, self._genre, self._marque, self._age)
    def band(self):
        x = input("what is the name of your band?")
        z = input("on a scale of 1 to 10 do they rock?")
        g = random.randrange(1,10)
        if g == z:
            print(True)
        else:
            print(False)



class Violon(Instruments_cordes):
    def __init__(self, nb_cordes, genre, marque, materiel):
        #matériel propre à violon
        super().__init__(nb_cordes, genre, marque)
        self._materiel = materiel

    def level(self):
        print("Your level is...")
        print("Shut up, I am perfect.")


bonjour = Instruments_cordes("5 strings", "METAL", "I MADE IT MYSELF")
red = Guitare("8 strings", "rock", "stratocaster", "4 ans", "metallica")
suzie = Violon("4 strings", "folk metal", "idk man", "wood")
suzanna = Instruments_cordes("5 strings", "folk metal", "idk man")

bonjour.level()
bonjour.info()
print("----------------")
red.info()
red.reinfo()
red.band()
print("----------------")
suzanna.level()
suzie.level()
#il y a deux levels: violon et instruments

#alloooooooooooooooo