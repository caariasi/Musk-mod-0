#Ejercicio 1

class Jet:
    def __init__(self, name, country):
        self.name = name
        self.country = country

frist_item = Jet("F16", "USA")   

print(frist_item.name)

#Ejercicio 2

second_item = Jet("SU33", "Russian")

thrid_item = Jet("AJS37", "Sweden")

fourth_item = Jet("Mirage2000", "France")

fifth_item = Jet("F14", "USA")

sixth_item = Jet("Mig29", "USSR")

seventh_item = Jet("A10", "USA")

#Ejercicio 3

class Jet:
    def __init__(self, name, country, cantidad):
        self.name = name
        self.country = country
        self.cantidad = cantidad
        

first_item = Jet("F14", "USA", input("Ingrese la cantidad del primer modelo "))

print("Las existencias del modelo {} son {}.".format(first_item.name, first_item.cantidad))


second_item = Jet("Mirage2000", "France", input("Ingrese la cantidad del segundo modelo "))

print("Las existencias del modelo {} son {}.".format(second_item.name, second_item.cantidad))



