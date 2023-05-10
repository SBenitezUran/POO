class Persona:
    def __init__(self, nombre, edad, profesion):
        self._nombre = nombre
        self._edad = edad
        self._profesion = profesion
        
    def saludar(self):
        print(f"Hola, soy {self._nombre}!")
        
    def presentarse(self):
        print(f"Mi nombre es {self._nombre}, tengo {self._edad} años y soy {self._profesion}.")
        
    def cambiar_profesion(self, nueva_profesion):
        self._profesion = nueva_profesion
        print(f"Acabo de cambiar mi profesión a {self._profesion}.")
        
        print("-------------------------------------------------------")
        
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    def get_edad(self):
        return self._edad
    
    def set_edad(self, nueva_edad):
        self._edad = nueva_edad
    
    def get_profesion(self):
        return self._profesion
    
    def set_profesion(self, nueva_profesion):
        self._profesion = nueva_profesion
        
        
Persona1 = Persona("Santiago", 25, "Conductor de trenes")

Persona1.saludar()
Persona1.presentarse()
Persona1.cambiar_profesion("Programador")

print(Persona1.get_nombre())
Persona1.set_nombre("Felipe")
print(Persona1.get_nombre())

print(Persona1.get_edad())
Persona1.set_edad(28)
print(Persona1.get_edad())

print(Persona1.get_profesion())
Persona1.set_profesion("Arquitecto")
print(Persona1.get_profesion())

print("------------------------------------------------------------------")

Persona1.saludar()
Persona1.presentarse()

print("===================================================================")



class Empleado(Persona):
    def __init__(self, nombre, edad, profesion, empresa):
        super().__init__(nombre, edad, profesion)
        self.empresa = empresa
        
    def trabajar(self):
        print(f"estoy trabajando ahora mismo en {self.empresa}.")

empleado1 = Empleado("Juan", 30, "Ingeniero", "Ruta N")

empleado1.saludar()
empleado1.presentarse()
empleado1.trabajar()





    
        