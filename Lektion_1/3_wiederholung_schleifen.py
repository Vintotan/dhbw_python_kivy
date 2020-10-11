# Schleifen mit if, elif, else

currency = "€"
# currency = str(input("Waehrung eingeben: "))

if currency == "$": # Abfrage muss einen Boolean ausgeben, also True oder False
    print("US-Dollar")
elif currency == "§":
    print("Britischer Pfund")
elif currency == "€":
    print("Euro")
else:
    print("Japanischer Yen")

# Schleifen mit for

for i in 1, 2, 3, 4: # i ist die Schleifenvariable
    print(i, i*i)

for n in range(1, 10): # range(1, 10, 1) = 1, 2, 3, 4, 5, 6, 7, 8, 9 | 1 ... Startwert (inklusiv); 10 ... Endwert (exklusiv); 1 ... Schrittweite (standardmaessig auf 1)
    print(n)

for n in range(10, 0, -1): # Rueckwaerts zaehlen
    print(n)

# Schleifen mit while

print("Menue:")
print("1: Heizstab ein")
print("2: Heizstab aus")
print("3: Programm beenden")

aktion = 0

#while aktion != 3:
#    aktion = int(input("Aktion waehlen (1, 2, 3): "))

    # Funktion ausfuehren
#    if aktion == 1:
#        print("Heizstab wird eingeschaltet.")
#    elif aktion == 2:
#        print("Heizstab wird ausgeschaltet.")
#    elif aktion == 3:
#        print("Programm wird beendet.")
#    else:
#        print("Ungueltige Eingabe")

while True:
    aktion = int(input("Aktion waehlen (1, 2, 3): "))

    # Funktion ausfuehren
    if aktion == 1:
        print("Heizstab wird eingeschaltet.")
    elif aktion == 2:
        print("Heizstab wird ausgeschaltet.")
    elif aktion == 3:
        print("Programm wird beendet.")
        break
    else:
        print("Ungueltige Eingabe")