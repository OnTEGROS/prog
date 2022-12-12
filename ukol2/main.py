import evidence
import os
import time

evi = evidence.Evidence()
choice = 0

while choice != "4":
    os.system("cls")
    print("Vyberte akci")
    print("1 - přidat nového pojištěnce")
    print("2 - vypsat všechny pojištěnce")
    print("3 - vyhledat pojištěného")
    print("4 - konec")
    choice = input()
    if choice == "1":
        evi.pridat()
    elif choice == "2":
        evi.vypsat()
    elif choice == "3":
        evi.vyhledat()
    elif choice != "4":
        print("Neplatné zadání!")
        time.sleep(2)

