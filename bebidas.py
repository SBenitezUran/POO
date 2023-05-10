class bebida:
    def __init__(self, clase, nombre, precio, sabor):
        self.clase = clase
        self._nombre = nombre
        self.precio = precio
        self._sabor = sabor
    
    def mostrar_informacion(self):
        print(f"Esta bebida es {self.clase} se llama {self._nombre} cuesta {self.precio} y su sabor es {self._sabor}")
    
    def es_mas_cara_que(self, otra_bebida):
        if self.precio > otra_bebida.precio:
            return True
        else:
            return False
        
    def get_nombre(self):
        return self._nombre
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
        
    def get_sabor(self):
        return self._sabor
    def set_sabor(self, nuevo_sabor):
        self._sabor = nuevo_sabor
    
bebida1 = bebida("Alcoholica", "Agila", 4500, "amargo")
bebida2 = bebida("Sin alcohol","Agua", 3000, "Neutro")

bebida1.mostrar_informacion()
bebida2.mostrar_informacion()
print(bebida1.es_mas_cara_que(bebida2))

print("--------------------------------------------------------------")

print(bebida1.get_nombre())
bebida1.set_nombre("Pilsen")
print(bebida1.get_nombre())

print(bebida1.get_sabor())
bebida1.set_sabor("Más amarga")
print(bebida1.get_sabor())

print("---------------------------------------------------------------")

bebida1.mostrar_informacion()

print("-----------------------------------------------------------------")

class saludables(bebida):
    def __init__(self, clase, nombre, precio, sabor, saludable):
        super().__init__(clase, nombre, precio, sabor)
        self.saludable = saludable
       
    def mejor(self):
        print(f"Esta bebida es {self.clase} se llama {self._nombre} cuesta {self.precio}, su sabor es {self._sabor} y {self.saludable}")
    
bebida3 = saludables("Sin alcohol", "Jugo de Guayaba", 2000, "dulce", "Viene de la Guayaba")
bebida3.mejor()
print(bebida3.es_mas_cara_que(bebida2))



