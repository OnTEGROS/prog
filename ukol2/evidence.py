import pojistenec as poj
import os
import time
import msvcrt
def wait():
    msvcrt.getch()

class Evidence:
    def __init__(self):
        self.seznam = []

    def pridat(self):
        os.system('cls')
        print("Zadejte jméno:")
        jmeno = str(input())
        print("Zadejte příjmení:")
        prijmeni = str(input())
        print("Zadejte věk:")
        vek = str(input())
        print("Zadejte tel. číslo:")
        cislo = str(input())

        self.seznam.append(poj.Pojistenec(jmeno, prijmeni, vek, cislo))
        print("")
        print("Pojištěnec úspešně přidán.")
        time.sleep(2)

    def vypsat(self):
        os.system('cls')
        for pojistenec in self.seznam:
            print(pojistenec.__str__())
        print("")
        print("Stiskněte cokoliv.")
        wait()
    
    def vyhledat(self):
        os.system('cls')
        print("Zadejte jméno:")
        jmeno = str(input())
        print("Zadejte příjmení:")
        prijmeni = str(input())
        os.system('cls')
        print("Výsledek:")
        print("")
        for pojistenec in self.seznam:
            if pojistenec.jmeno == jmeno and pojistenec.prijmeni == prijmeni:
                print(pojistenec)
        print("")
        print("Stiskněte cokoliv.")
        wait()