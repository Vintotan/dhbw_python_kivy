# Datentypen

## Strings - Zeichenketten

Erster_Name = "DHBW" # -> Camel Case
erster_name = "DHBW" # -> Snake Case -> Favorit in Python
Zweiter_Name = ' Stuttgart'
Name = Erster_Name + Zweiter_Name

# Regeln für Variablenbezeichnungen:
# - darf nicht mit einer Zahl beginnen
# - Groß- und Kleinschreibung beachten
# - Unterstriche erlaubt
# - Keywords nicht gestattet

print(Name)

print(len(Name))

import keyword
print(keyword.kwlist)

## Booleans - Binaere Werte / Zustaende

print(True)
print(False)

## Integers - Ganze Zahlen

zwanzig = 20

print(zwanzig)
zwanzig_zweiter_name = str(zwanzig) + Zweiter_Name
print(zwanzig_zweiter_name)

## Float - Gleitpunktzahlen / Dezimalzahlen
promille_auto = 0.5
promille_club = 1.0

int_promille_club = 1.0

print(promille_club)
print(int(promille_club))

print(float(zwanzig))

int_promille_club = "Eins Komma Null"
print(int_promille_club)

## Konstanten nicht sicher abspeicherbar
PI = 3.141592
PI = "python"