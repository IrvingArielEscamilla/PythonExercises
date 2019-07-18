class Persona:

    def __init__(self,edad,nombre):
        self.edad = edad
        self.nombre = nombre
        print("Se ha creado a",self.nombre, "de",self.edad)

    def hablar (self,**palabras ):
        for frase in palabras:
            print(self.nombre,":",palabras[frase])

juan = Persona(18,"Juan")
luis = Persona(20,"Luis")
juan.hablar(t1 ="hola estoy hablando",t2 ='Este soy yo')
luis.hablar(t1 ="Me cago",t2="y ahora q?")