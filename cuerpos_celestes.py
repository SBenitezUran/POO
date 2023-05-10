class CuerpoCeleste:
    def __init__(self, nombre, tipo, masa, diametro):
        self._nombre = nombre
        self.tipo = tipo
        self._masa = masa
        self._diametro = diametro
        
    def mostrar_informacion(self):
        print(f"{self._nombre} es un {self.tipo} con una masa de {self._masa} kg y un diámetro de {self._diametro} km.")
        
    def orbitar(self, otro_cuerpo):
        print(f"{self._nombre} está orbitando a {otro_cuerpo._nombre}.")
        
    def get_nombre(self):
        return self._nombre
    def set_nombre(self, otro_nombre):
        self._nombre = otro_nombre
    
    def get_masa(self):
        return self._masa
    def set_masa(self, otra_masa):
        self._masa = otra_masa
        
    def get_diametro(self):
        return self._diametro
    def set_diametro(self, otro_diametro):
        self._diametro = otro_diametro
        
        

sol = CuerpoCeleste("Sol", "estrella", 1.9885 * 10**30, 1.3927 * 10**6)
sol.mostrar_informacion() 
tierra = CuerpoCeleste("Tierra", "planeta", 5.972 * 10**24, 12.742)
tierra.mostrar_informacion() 
tierra.orbitar(sol) 

print("----------------------------------------------------------------")

print(tierra.get_nombre())
tierra.set_nombre("Marte")
print(tierra.get_nombre())

print(tierra.get_masa())
tierra.set_masa(6.39 * 10**23)
print(tierra.get_masa())

print(tierra.get_diametro())
tierra.set_diametro(6.779)
print(tierra.get_diametro())

print("---------------------------------------------------------------------")

tierra.mostrar_informacion()

print("-----------------------------------------------------------------------")


class Satelite(CuerpoCeleste):
    def __init__(self, nombre, tipo, masa, diametro, orbita):
        super().__init__(nombre, tipo, masa, diametro)
        self.orbita = orbita
        
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Este satélite orbita alrededor de la {self.orbita}")
        
luna = Satelite("Luna", "satélite natural", 7.342 * 10**22, 3_474, "tierra")
luna.mostrar_informacion()




    


        
