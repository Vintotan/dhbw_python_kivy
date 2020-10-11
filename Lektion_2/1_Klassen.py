from math import *


class vector(object):
    x = None  # Klassenattribut
    y = None  # Klassenattribut

    def vorgabe(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def rueckgabe(self):
        return self.x, self.y

    def eingabe(self):
        self.x = float(input("Bitte die x-Komponente eingeben: "))
        self.y = float(input("Bitte die y-Komponente eingeben: "))

    def ausgabe(self):
        if self.x == None or self.y == None:
            print("Es wurde noch kein Vektor defininert!")
        else:
            betrag = sqrt(self.x**2 + self.y**2)

            print("X-Komponente: ", self.x)
            print("Y-Komponente: ", self.y)

            print("Der Betrag ist: ", betrag)


# v = vector()  # Erzeugt ein Objekt aus der Klasse vector und speichert diesen in der Variable v

# v.eingabe()  
# v.ausgabe()

# v.rueckgabe()
# v.ausgabe()

u = vector() 
u.vorgabe(2, 3)  # 2, 3 sind Argumente und werden an die Parameter x, y übergeben
u.ausgabe()
