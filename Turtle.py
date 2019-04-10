from Fish import Fish
#Nombre: Turtle(Tipo:Class)
#Objetivo: crea objetos tipo Turtle con parametros que hereda de la clase Fish
class Turtle(Fish):
    def __init__(self, name, water, size, temperature, country, amount):
        Fish.__init__(self, name, water, size, temperature, country, amount)
        self.set_type("TORTUGA")