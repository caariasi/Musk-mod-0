#Ejercicio 8
'''
class Estudiante:
        
    def calcular_media(self, notas):
        self.grade = sum(notas) / len(notas)
        return self.grade
    
    @staticmethod
    def Asinaturas_reprobadas(asignaturas, notas):
        if len(notas) != len(asignaturas):
            print("las notas y las asignaturas no coinciden")
            return
        
        for asignatura, nota in zip(asignaturas, notas):
            if nota < 5:
                print("Asignatura: {} - Nota: {}".format(asignatura, nota))
                
                
estudiante1 = Estudiante()

notas = [3,8,10,4,7]

asignaturas = ["Diccionario","Quimica","Ingles","Lengua","Deportes"]

estudiante1.Asinaturas_reprobadas(asignaturas, notas)


#Ejercicio 9

class Estudiante:
        
    def calcular_media(self, notas):
        self.grade = sum(notas) / len(notas)
        return self.grade
    
    @staticmethod
    def Asinaturas_reprobadas(asignaturas, notas):
        if len(notas) != len(asignaturas):
            print("las notas y las asignaturas no coinciden")
            return
        
        for asignatura, nota in zip(asignaturas, notas):
            if nota < 5:
                print("Asignatura: {} - Nota: {}".format(asignatura, nota))
                
    escuela = "Escuela publica"
    
    @classmethod
    def cambiar_escuela(cls, nueva_escuela):
        cls.escuela = nueva_escuela
        

estudiante1 = Estudiante()

print("escuela inicial: {}".format(estudiante1.escuela))

estudiante1.cambiar_escuela("Escuela privada")

print("escuela final: {}".format(estudiante1.escuela))

'''
#Ejercicio 10

class Estudiante:
        
    def calcular_media(self, notas):
        self.grade = sum(notas) / len(notas)
        return self.grade
    
    @staticmethod
    def Asinaturas_reprobadas(asignaturas, notas):
        if len(notas) != len(asignaturas):
            print("las notas y las asignaturas no coinciden")
            return
        
        for asignatura, nota in zip(asignaturas, notas):
            if nota < 5:
                print("Asignatura: {} - Nota: {}".format(asignatura, nota))
                
    escuela = "Escuela publica"
    
    @classmethod
    def cambiar_escuela(cls, nueva_escuela):
        cls.escuela = nueva_escuela
        
    def _comprobar_asistencia(self, asistencia):
        resultados = {}
        
        for mes, numero_asistencias in asistencia.items():
            if numero_asistencias < 4:
                resultados[mes] = 1
            elif 4 <= numero_asistencias < 8:
                resultados[mes] = 2
            else:
                resultados[mes] = 3
        return resultados
    
    def imprimir_asistencia(self, asistencia):
        return self._comprobar_asistencia(asistencia)
    
    
estudiante1 = Estudiante()

asistencia = {
    "septiembre": 4,
    "octubre": 8,
    "noviembre": 2,
    "diciembre": 6
}

resultados = estudiante1.imprimir_asistencia(asistencia)

for mes, evaluacion in resultados.items():
    print("Mes: {}, Evaluacion {}".format(mes,evaluacion))
    