class Automobil(object):  # Oberklasse / Superklasse
    antrieb = "Ottomotor"
    leistung_in_kw = 120

    def ausgabe(self):
        print("Antrieb: ", self.antrieb)
        print("Leistung: ", self.leistung_in_kw)


class PKW(Automobil):  # Unterklasse / Subklasse
    pass


print("Automobil a: ")
a = Automobil()
a.ausgabe()

print("PKW b: ")
b = PKW()
b.ausgabe()

# Mehrfachvererbung

class lkw(object):  # object sorgt dafuer, dass die Klasse lkw nur vererben kann
    ladeflaeche = 6

    def ausgabe_lkw(self):
        print("Ladeflaeche in qm: ", self.ladeflaeche)


class pkw(object):
    sitzplaetze = 4

    def ausgabe_pkw(self):
        print("Sitzplaetze: ", self.sitzplaetze)


class pick_up(lkw, pkw):
    motorleistung = 120

    def ausgabe(self):
        self.ausgabe_lkw()
        self.ausgabe_pkw()
        print("Motorleistung in KW: ", self.motorleistung)


print("LKW c:")
c = lkw()
c.ausgabe_lkw

print("Pick-Up d:")
d = pick_up()
d.ausgabe()
