class Citire:
    def __init__(self):
        self.citiri = {}

    def adauga_citire(self, an, luna, apa_rece, apa_calda):
        cheie = (an, luna)
        if cheie in self.citiri:
            print("Eroare: Citirea pentru aceasta luna exista deja.")
            return

        if self.validare_citire(an, luna, apa_rece, apa_calda):
            self.citiri[cheie] = {'apa_rece': apa_rece, 'apa_calda': apa_calda}
            print("Citire adaugata cu succes.")
        else:
            print("Eroare: Datele introduse nu sunt valide.")

    def sterge_citire(self, an, luna):
        cheie = (an, luna)
        if cheie in self.citiri:
            del self.citiri[cheie]
            print("Citire ștearsa cu succes.")
        else:
            print("Eroare: Nu exista o citire pentru aceasta luna.")

    def afiseaza_consum(self, an, luna):
        cheie_curenta = (an, luna)
        cheie_precedenta = self.calculeaza_luna_precedenta(an, luna)

        if cheie_curenta in self.citiri and cheie_precedenta in self.citiri:
            consum_apa_rece = self.citiri[cheie_curenta]['apa_rece'] - self.citiri[cheie_precedenta]['apa_rece']
            consum_apa_calda = self.citiri[cheie_curenta]['apa_calda'] - self.citiri[cheie_precedenta]['apa_calda']

            print(f"Consum apa rece: {consum_apa_rece} unitati")
            print(f"Consum apa calda: {consum_apa_calda} unitati")
        else:
            print("Eroare: Nu exista citiri pentru luna curenta si luna precedenta.")

    def validare_citire(self, an, luna, apa_rece, apa_calda):
        if luna not in ['ian', 'feb', 'mar', 'apr', 'mai', 'iun', 'iul', 'aug', 'sep', 'oct', 'noi', 'dec']:
            return False

        if (an, luna) in self.citiri:
            return False

        if apa_rece < 0 or apa_calda < 0:
            return False

        cheie_precedenta = self.calculeaza_luna_precedenta(an, luna)
        if cheie_precedenta in self.citiri:
            if apa_rece < self.citiri[cheie_precedenta]['apa_rece'] or apa_calda < self.citiri[cheie_precedenta][
                'apa_calda']:
                return False

        return True

    def calculeaza_luna_precedenta(self, an, luna):
        luni = ['ian', 'feb', 'mar', 'apr', 'mai', 'iun', 'iul', 'aug', 'sep', 'oct', 'noi', 'dec']
        index_luna = luni.index(luna)

        if index_luna == 0:
            an_precedent = an - 1
            luna_precedenta = luni[-1]
        else:
            an_precedent = an
            luna_precedenta = luni[index_luna - 1]

        return (an_precedent, luna_precedenta)

#Exemplu de utilizare
adauga_citiri = Citire()

# Adaugare citire
adauga_citiri.adauga_citire(an=2023, luna='ian', apa_rece=50, apa_calda=25)
#adauga_citiri.adauga_citire(an=2023, luna='feb', apa_rece=50, apa_calda=25)

#Afisare consum pentru luna curenta
#adauga_citiri.afiseaza_consum(an=2023, luna='feb')

#Stergere citire
#adauga_citiri.sterge_citire(an=2023, luna='ian')

