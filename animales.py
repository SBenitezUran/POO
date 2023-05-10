class Animal:
    def __init__(self, especie, nombre, edad):
        self.especie = especie
        self._nombre = nombre
        self._edad = edad
        
    def emitir_sonido(self):
        print(f"El {self.especie} {self._nombre} emite un sonido.")
    def moverse(self):
        print(f"El {self.especie} {self._nombre} se mueve de alguna forma.")
    def mostrar_información(self):
        print(f"Este animal es un {self.especie}, llamado {self._nombre} y tiene {self._edad} años.")
    
    def get_nombre(self):
        return self._nombre
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    def get_edad(self):
        return self._edad
    def set_edad(self, otra_edad):
        self._edad = otra_edad
        
perro = Animal("perro", "retsu", 2)
gato = Animal("gato", "pimienta", 3)

perro.emitir_sonido()
perro.moverse()
perro.mostrar_información()

print("---------------------------------------------------------------------")

gato.emitir_sonido()
gato.moverse()
gato.mostrar_información()

print("---------------------------------------------------------------------")

print(perro.get_nombre())
perro.set_nombre("Toby")
print(perro.get_nombre())

print(gato.get_edad())
gato.set_edad("6")
print(gato.get_edad())

print("----------------------------------------------------------------------")

perro.mostrar_información()
gato.mostrar_información()

print("----------------------------------------------------------------------")

class salvaje(Animal):
    def __init__(self, especie, nombre, edad, rango):
        super().__init__(especie, nombre, edad)
        self.rango = rango
        
    def agresivo(self):
        print(f"Este animal es un {self.especie}, se llama {self._nombre}, tiene {self._edad} años y es el {self.rango} ")
        
Leon = salvaje("felino", "Mapumba", 4, "Rey de la selva")
Leon.emitir_sonido()
Leon.moverse()
Leon.agresivo()

print("---------------------------------------------------------------------")

class domestico(Animal):
    def __init__(self, especie, nombre, edad, tipo):
        super().__init__(especie, nombre, edad)
        self.tipo = tipo
        
    def tranquilo(self):
        print(f"Este animal es un {self.especie}, se llama {self._nombre}, tiene {self._edad} años y es un {self.tipo}")

loro = domestico("ave", "Lupe", 3, "oviparo")
loro.emitir_sonido()
loro.moverse()
loro.tranquilo()


    
        


        
        


        

        

