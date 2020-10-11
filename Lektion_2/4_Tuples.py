werte_1 = (10, 20, 30) # -> Favorit
werte_2 = 10, 20, 30

print(werte_1)
print(werte_2)

if werte_1 == werte_2:
    print("Tuples identisch")
else:
    print("nicht identisch")

# Tuples sind eine geordnete Zusammenfassung beliebiger Objekte
# Unterschied zu Listen: Tuples sind unveraenderlich

# werte_1.append(40) -> funktioniert nicht, da Tuples unveraenderlich sind
print(werte_1)