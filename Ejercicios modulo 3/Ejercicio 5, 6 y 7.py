#Ejercicio 5

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
estudiante1 = Estudiante("juan", 13, "octavo grado")

print(estudiante1.nombre)
print(estudiante1.edad)
print(estudiante1.grado)

#Ejercicio 6

class Estudiante:
    pass

estudiante2 = Estudiante()

print(type(estudiante2))

#Ejercicio 7

class Estudiante:
        
    def calcular_media(self, notas):
        self.grade = sum(notas) / len(notas)
        return self.grade
    
estudiante3 = Estudiante()

notas = [10,7,6,9,3]

print("la media del estudiate es: {}".format(estudiante3.calcular_media(notas)))