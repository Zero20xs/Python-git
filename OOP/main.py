from car import Car
from account import Account

if __name__ == "__main__":
    jls_extract_var = print
    jls_extract_var ("hola mundo")
    car = Car("AMS234", Account(" Camilo paz", "A94482505"))
    print(vars(car))
    print(vars(car.Driver))


"""
    car2 = Car()
    car2.License = " QWE602"
    car2.driver = " Pepa peerz"
    print (vars(car2))
"""
