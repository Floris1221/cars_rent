from datetime import date
import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",password="",database="samochody")

mycursor = db.cursor()


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
            self.data_wyp = date.today()
            print("Podaj id klienta")
            self.id_kli = int(input())
            print("Podaj id samochodu")
            self.id_sam = int(input())
            print("Podaj rok końca wypożyczenia")
            rok = int(input())
            print("Podaj miesiąc końca wypożyczenia")
            miesiac = int(input())
            print("Podaj dzień końca wypożyczenia")
            dzien = int(input())
            self.data_kon = date(rok,miesiac,dzien)
            print("Podaj należność")
            self.kwota = int(input())
            self.add_query()
        except:
            print("Podano nie poprawne wartości.\n Wciśnij 1 aby ponownie wpisać dane, dowolny inny aby wyjść")
            x = int(input())
            if (x == 1):
                self.add_rent()
            else:
                print("Powrót do menu")

    def display_rent_by_id(self):
        self.display_query()

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




    def add_query(self):
        try:
            mycursor.execute(
                "INSERT INTO wypozyczenia (idklienta,idauta,datawyp,datazwrotu,naleznosc) VALUES (%s,%s,%s,%s,%s)",
                (self.id_kli, self.id_sam, self.data_wyp, self.data_kon, self.kwota))
            db.commit()
            print("Dodawanie powiodło się")
        except Exception as e:
            print(e)


    def display_query(self):
        try:
            mycursor.execute("SELECT w.idwyp, k.imie, k.nazwisko, k.idklienta, a.model, a.idauta, w.datawyp, w.datazwrotu, w.naleznosc FROM klienci AS k,auta AS a,wypozyczenia AS w WHERE a.idauta=w.idauta AND k.idklienta = w.idklienta ORDER BY w.datawyp DESC")
            for x in mycursor:
                print(x)
        except Exception as e:
            print(e)


