# Dictionary ist eine ungeordnete Zusammenfassung von Schluessel-Wert-Paaren 

kfz = {"DO": "Dortmund", "S": "Stuttgart", "B": "Berlin,", "HB": "Bremen", "Dortmund": "BVB"}

print(kfz["DO"])  # -> Abfrage ueber Key-Value => Ausgabe des Data-Value
print(kfz["Dortmund"])  # -> jeder Key-Value muss einzigartig sein

neu = {}
print(type(neu))
print(neu)