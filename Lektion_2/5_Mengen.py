listen = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(listen)

tuples = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
print(tuples)

menge = set([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
print(menge)

# Menge / Set ist eine ungeordnete Zusammenfassung von Objekten, wobei jedes Element nur einmal darin vorkommen darf
# Listen können keine Elemente von Mengen sein

Menge_1 = set([1, 3, 5, 7])
Menge_2 = set([2, 4, 6, 8])

# Durchschnitt / Schnittmenge
durchschnitt = Menge_1 & Menge_2
print(durchschnitt)

# Vereinigung
vereinigung = Menge_1 | Menge_2
print(vereinigung)

for i in Menge_1:
    print(i)