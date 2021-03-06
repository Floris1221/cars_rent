import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",password="",database="samochody")

mycursor = db.cursor()


class Cars:
    def __init__(self,excercse):
        if(excercse==1):
            self.add_car()
        elif(excercse==2):
            self.display_car_by_id()
        elif(excercse==3):
            self.edit_car_by_id()



    def add_car(self):
        try:
            print("Podaj marke")
            self.marka = input()
            print("Podaj model")
            self.model = input()
            print("Podaj przebieg")
            self.przebieg = int(input())
            print("Podaj rocznik")
            self.rocznik = int(input())
            print("Podaj kolor")
            self.kolor = input()
            print("Podaj ubezpieczenie")
            self.ubezpieczenie = int(input())
            self.add_query()
        except:
            print("Podano nie poprawne wartości.\n Wciśnij 1 aby ponownie wpisać dane, dowolny inny aby wyjść")
            x = int(input())
            if(x==1):
                self.add_car()
            else:
                print("Powrót do menu")



    def display_car_by_id(self):
        print("Podaj id samochodu")
        try:
            self.id = int(input())
            self.display_query()
        except:
            print("Podano nie poprawne wartości.\n Wciśnij 1 aby ponownie wpisać dane, dowolny inny aby wyjść")
            x = int(input())
            if (x == 1):
                self.display_car_by_id()
            else:
                print("Powrót do menu")




    def edit_car_by_id(self):
        print("Podaj id samochodu")
        try:
            self.id = int(input())
        except:
            print("Podano nie poprawne wartości.\n Wciśnij 1 aby ponownie wpisać dane, dowolny inny aby wyjść")
            x = int(input())
            if (x == 1):
                self.edit_car_by_id()
            else:
                print("Powrót do menu")


    def add_query(self):
        try:
            mycursor.execute("INSERT INTO auta (marka,model,przebieg,rocznik,kolor,ubezpieczenie) VALUES (%s,%s,%s,%s,%s,%s)",(self.marka,self.model,self.przebieg,self.rocznik,self.kolor,self.ubezpieczenie))
            db.commit()
            print("Dodawanie powiodło się")
        except Exception as e:
            print(e)



    def display_query(self):
        try:
            sql_select_query = "SELECT * FROM auta WHERE idauta= %s"
            mycursor.execute(sql_select_query,(self.id,))
            print(mycursor.fetchone())
        except Exception as e:
            print(e)
