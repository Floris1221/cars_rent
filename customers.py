import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",password="",database="samochody")

mycursor = db.cursor()

class Customer:
    def __init__(self,excercse):
        if (excercse == 1):
            self.add_customers()
        elif (excercse == 2):
            self.display_customer_by_id()
        elif (excercse == 3):
            self.edit_customer_by_id()



    def add_customers(self):
        try:
            print("Podaj imię")
            self.imie = input()
            print("Podaj nazwisko")
            self.nazwisko = input()
            print("Podaj dowód")
            self.dowod = input()
            print("Podaj adres")
            self.adres = input()
            print("Podaj miasto")
            self.miasto = input()
            print("Podaj płeć")
            self.plec = input()
            self.add_query()
        except:
            print("Podano nie poprawne wartości.\n Wciśnij 1 aby ponownie wpisać dane, dowolny inny aby wyjść")
            x = int(input())
            if (x == 1):
                self.add_customers()
            else:
                print("Powrót do menu")


    def display_customer_by_id(self):
        print("Podaj id klienta")
        try:
            self.id = int(input())
            self.display_query()
        except:
            print("Podano nie poprawne wartości.\n Wciśnij 1 aby ponownie wpisać dane, dowolny inny aby wyjść")
            x = int(input())
            if (x == 1):
                self.display_customer_by_id()
            else:
                print("Powrót do menu")



    def edit_customer_by_id(self):
        print("Podaj id klienta")
        try:
            self.id = int(input())
        except:
            print("Podano nie poprawne wartości.\n Wciśnij 1 aby ponownie wpisać dane, dowolny inny aby wyjść")
            x = int(input())
            if (x == 1):
                self.edit_customer_by_id()
            else:
                print("Powrót do menu")




    def add_query(self):
        try:
            mycursor.execute(
                "INSERT INTO klienci (imie,nazwisko,dowod,adres,miasto,plec) VALUES (%s,%s,%s,%s,%s,%s)",
                (self.imie, self.nazwisko, self.dowod, self.adres, self.miasto, self.plec))
            db.commit()
            print("Dodawanie powiodło się")
        except Exception as e:
            print(e)

    def display_query(self):
        try:
            sql_select_query = "SELECT * FROM klienci WHERE idklienta= %s"
            mycursor.execute(sql_select_query, (self.id,))
            print(mycursor.fetchone())
        except Exception as e:
            print(e)