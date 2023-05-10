class Textos:
    def __init__(self, texto):
        self.texto = texto
        self.cantidad_palabras = len(self.texto.split())
        self.cantidad_caracteres = len(self.texto.replace(" ", ""))
    
        
    def palabras(self):
        return self.cantidad_palabras
    
    def caracteres(self):
        return self.cantidad_caracteres
    
    def mayusculas(self):
        return self.texto.upper() 
    
    def minusculas(self):
        return self.texto.lower()
    
    def reemplazar_palabra(self, palabra_a_reemplazar, nueva_palabra):
        return self.texto.replace(palabra_a_reemplazar, nueva_palabra)
    
    def mostrar_info(self):
        print(f"Texto: {self.texto}")
        print(f"Cantidad de palabras: {self.cantidad_palabras}")
        print(f"Cantidad de caracteres: {self.cantidad_caracteres}")
        print(f"Texto en mayúsculas: {self.mayusculas()}")
        print(f"Texto en minúsculas: {self.minusculas()}")
        print(f"Texto con reemplazo de palabra: {self.reemplazar_palabra('ejemplo', 'texto')}")
        
texto_ejemplo= "Hola mundo, este es un ejemplo de texto para trabajar."
Texto1 = Textos(texto_ejemplo)
Texto1.mostrar_info()
texto_modificado = Texto1.reemplazar_palabra("ejemplo", "texto")

print("=================================================================")

class Parrafo(Textos):
    def __init__(self, texto, ortografía):
        super().__init__(texto)
        self.ortografía = ortografía
    
    def calidad(self):
        return  f"Este texto tiene buena {self.ortografía}"
        
Parrafo_ejemplo = "Hola, mi nombre es Santiago y me gustan muchas cosas, por ejemplo la programación"
Parrafo1 = Parrafo(Parrafo_ejemplo, "ortografia")
Parrafo1.mostrar_info()
print(Parrafo1.calidad())






        
    




