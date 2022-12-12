class Pojistenec:
    def __init__(self, jmeno, prijmeni, vek, cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.cislo = cislo

    def __str__(self):
        return f"jméno: {self.jmeno}\npříjmení: {self.prijmeni}\nvěk: {self.vek}\ntel. číslo: {self.cislo}"