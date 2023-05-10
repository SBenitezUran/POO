class materias:
    def __init__(self,  nombre, dificultad, semestre):
        self._nombre = nombre
        self._dificultad = dificultad
        self.semestre = semestre
    
    def mostrar_información(self):
        print(f"Esta materia se llama {self._nombre}, tiene un grado de dificultad {self._dificultad} y es del {self.semestre} semestre")
    
    def get_nombre(self):
        return self._nombre
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    def get_dificultad(self):
        return self._dificultad
    def set_dificultad(self, nueva_dificultad):
        self._dificultad = nueva_dificultad
    
        
Materia = materias("Cálculo integral", "alto", 4)
Materia.mostrar_información()

print("--------------------------------------------------------------------------")

print(Materia.get_nombre())
Materia.set_nombre("Inglés")
print(Materia.get_nombre())

print(Materia.get_dificultad())
Materia.set_dificultad("Intermedio")
print(Materia.get_dificultad())

print("--------------------------------------------------------------------------------")

Materia.mostrar_información()

print("----------------------------------------------------------------------------------")

class cursos(materias):
    def __init__(self, nombre, dificultad, semestre, profesor):
        super().__init__(nombre, dificultad, semestre)
        self.profesor = profesor
    
    def recomendado(self):
        print(f"Este curso se llama {self._nombre}, tiene una dificultad {self._dificultad}, es del {self.semestre} semestre y la da el profesor {self.profesor}")
        
curso1 = cursos("Matemáticas especiales", "alto", "5", "Raul")
curso1.recomendado()
    