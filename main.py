# import mysql.connector
from cars import Cars

# db = mysql.connector.connect(host="localhost",user="root",password="",database="samochody")
#
# mycursor = db.cursor()

#menu
def menu():
    print("1. Samochody")
    print("2. Klienci")
    print("3. Wypożyczenia")
    print("4. Wyjście")
    try:
        x=int(input())
        choice(x)
    except:
        print("Podano nie poprawną wartość sprubój ponownie")
        menu()



def car_menu():
    print("1. Dodaj samochód")
    print("2. Usuń samochód")
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
    print("1. Dodaj klienta")
    print("2. Usuń klienta")
    print("3. Edytuj klienta")
    print("4. Wróć")
    x = int(input())


def rent_menu():
    print("1. Dodaj wypożyczenie")
    print("2. Usuń wypożyczenie")
    print("3. Edytuj wypożyczenie")
    print("4. Wróć")
    x = int(input())


def choice(x):
    if(x==1):
        car_menu()
    elif(x==2):
        customer_menu()
    elif(x==3):
        rent_menu()
    elif(x==4):
        exit()
    else:
        print("Podano nie poprawna wartość")
        menu()


def main():
    menu()

if __name__ == '__main__':main()



