# Ejercicio 10 modificado

# Modificare este codigo para que se puedan ingresar los datos del estudiante, nombre, edad, grado y sus asistencias
# Usare la funcion calcular_media para calcular el promedio de asistencia del estudiante
# Finalmente imprimire en pantalla los datos del estudiante y su promedio de asistencia

# Prueba de nueva rama

class Estudiante:

    def __init__(self):
        self.nombre = input("Ingrese el nombre del estudiante: ")
        self.edad = input("Ingrese la edad del estudiante: ")
        self.grado = input("Ingrese el grado del estudiante: ")
   
    def calcular_media(self, valores):
        self.grade = sum(valores) / len(valores)
        return int(self.grade)
    
    @staticmethod
    def asinaturas_reprobadas(asignaturas, notas):
        if len(notas) != len(asignaturas):
            print("las notas y las asignaturas no coinciden")
            return
        
        for asignatura, nota in zip(asignaturas, notas):
            if nota < 5:
                print(f"Asignatura: {asignatura} - Nota: {nota}")
                
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
    "Enero": 0, "Febrero": 0, "Marzo": 0, "Abril": 0, "Mayo": 0,
    "Junio": 0, "Julio": 0, "Agosto": 0, "Septiembre": 0,
    "Octubre": 0, "Noviembre": 0, "Diciembre": 0
}

for mes in asistencia.keys():
    while True:
        try:
            numero_asistencias = int(input(f"Ingrese las asistencias de {mes}: "))
            if numero_asistencias < 0:
                raise ValueError
            asistencia[mes] = numero_asistencias
            break
        except ValueError:
            print("Ingrese un número válido.")
            continue

print("\n" * 100)

resultados = estudiante1.imprimir_asistencia(asistencia)

media_asistencias = estudiante1.calcular_media(list(resultados.values()))
print(f"La media de asistencia anual del estudiante {estudiante1.nombre} de {estudiante1.edad} años que cursa el {estudiante1.grado}º es: {media_asistencias}","\n" * 10)
    