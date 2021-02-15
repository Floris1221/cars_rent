from datetime import date



class Rent:
    def __init__(self,excercse):
        if (excercse == 1):
            self.add_rent()
        elif (excercse == 2):
            self.display_rent_by_id()
        elif (excercse == 3):
            self.edit_rent_by_id()

    def add_rent(self):
        try:
            print("Podaj id klienta")
            self.id_kli = int(input())
            print("Podaj id samochodu")
            self.id_sam = int(input())
            print("Podaj date wypożyczenia")
            self.data_wyp = date(input())
            print("Podaj date końca wypożyczenia")
            self.data_kon = date(input())
            print("Podaj należność")
            self.kwota = int(input())
        except:
            print("Podano nie poprawne wartości.\n Wciśnij 1 aby ponownie wpisać dane, dowolny inny aby wyjść")
            x = int(input())
            if (x == 1):
                self.add_rent()
            else:
                print("Powrót do menu")

    def display_rent_by_id(self):
        print("Podaj id wypożyczenia")
        try:
            self.id = int(input())
        except:
            print("Podano nie poprawne wartości.\n Wciśnij 1 aby ponownie wpisać dane, dowolny inny aby wyjść")
            x = int(input())
            if (x == 1):
                self.display_rent_by_id()
            else:
                print("Powrót do menu")

    def edit_rent_by_id(self):
        print("Podaj id wypożyczenia")
        try:
            self.id = int(input())
        except:
            print("Podano nie poprawne wartości.\n Wciśnij 1 aby ponownie wpisać dane, dowolny inny aby wyjść")
            x = int(input())
            if (x == 1):
                self.edit_rent_by_id()
            else:
                print("Powrót do menu")
