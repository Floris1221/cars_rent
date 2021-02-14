
class Cars:
    def __init__(self,exercise):
        if(exercise==1):
            self.add_car()
        elif(exercise==2):
            self.display_car_by_id()
        elif(exercise==3):
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
        except:
            print("Podano nie poprawne wartości.\n Wciśnij 1 aby ponownie wpisać dane, dowolny inny aby wyjść")
            try:
                x = int(input())
                if(x==1):
                    self.add_car()
                else:
                    pass

            except:
                print("Podano nie poprawne wartości spróbuj ponownie")


    def display_car_by_id(self):
        print("Podaj id samochodu")
        try:
            self.id = int(input())
        except:
            print("Podano nie poprawną wartość")
            self.display_car_by_id()

    def edit_car_by_id(self):
        print("Podaj id samochodu")
        try:
            self.id = int(input())
        except:
            print("Podano nie poprawną wartość")
            self.edit_car_by_id()