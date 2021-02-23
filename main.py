
from cars import Cars
from customers import Customer
from rents import Rent



#menu
def menu():
    x=0
    print("1. Samochody")
    print("2. Klienci")
    print("3. Wypożyczenia")
    print("4. Wyjście")
    try:
        x=int(input())
        choice(x)
    except Exception as e:
        print("Podano nie poprawną wartość sprubój ponownie")
        menu()



def car_menu():
    y=0
    while (y!=4):
        print("1. Dodaj samochód")
        print("2. Wyświetl samochód")
        print("3. Edytuj samochód")
        print("4. Wróć")
        try:
            y=int(input())
            if (0 < y < 4):
                car = Cars(y)
            elif (y == 4):
                menu()
            else:
                print("Podano nie poprawną wartość. Spróbuj ponownie")
                car_menu()
        except:
            print("Podano nie poprawną wartość sprubój ponownie")
            car_menu()


def customer_menu():
    y=0
    while(y!=4):
        print("1. Dodaj klienta")
        print("2. Wyświetl klienta")
        print("3. Edytuj klienta")
        print("4. Wróć")
        try:
            y = int(input())
            if (0 < y < 4):
                customer = Customer(y)
            elif (y == 4):
                menu()
            else:
                print("Podano nie poprawną wartość. Spróbuj ponownie")
                customer_menu()
        except:
            print("Podano nie poprawną wartość sprubój ponownie")
            customer_menu()


def rent_menu():
    y=0
    while(y!=4):
        print("1. Dodaj wypożyczenie")
        print("2. Wyświetl wypożyczenie")
        print("3. Edytuj wypożyczenie")
        print("4. Wróć")
        try:
            y = int(input())
            if (0 < y < 4):
                rent = Rent(y)
            elif (y == 4):
                menu()
            else:
                print("Podano nie poprawną wartość. Spróbuj ponownie")
                rent_menu()
        except:
            print("Podano nie poprawną wartość sprubój ponownie")
            rent_menu()


def choice(x):
    if(x==1):
        car_menu()
    elif(x==2):
        customer_menu()
    elif(x==3):
        rent_menu()
    elif(x==4):
        print("Dziękuje za prace")
    else:
        print("Podano nie poprawna wartość")
        menu()


def main():
    menu()

if __name__ == '__main__':main()



