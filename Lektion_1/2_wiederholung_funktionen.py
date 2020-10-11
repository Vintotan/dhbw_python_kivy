# Berechnung von Umfang und Flaeche eines Kreises mithilfe einer Funktion

from math import pi 

w = "global"

def ausgabe(x, y): # x und y sind Parameter
    print("Die Flaeche ist {0}".format(y)) 
    print("Der Umfang ist {0}".format(x))
    print("Der Umfang ist {0} und die Flaeche ist {1}".format(x, y))
    print()
    print(w)
    r = "lokal"
    print(r)

# Kreis
radius = 10.0
umfang_kreis = 2 * pi * radius
flaeche_kreis = pi * radius ** 2 
ausgabe(umfang_kreis, flaeche_kreis) # umfang_kreis und flaeche_kreis sind Argumente

# Rechteck
hoehe = 10.0
breite = 50.0
umfang_rechteck = 2 * (hoehe + breite)
flaeche_rechteck = breite * hoehe
ausgabe(umfang_rechteck, flaeche_rechteck)

# print(r)
