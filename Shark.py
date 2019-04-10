from Fish import Fish

#Nombre: Shark(Tipo:Class)
#Objetivo: crea objetos tipo Tiburon con parametros que hereda de la clase Fish
class Shark(Fish):
    def __init__(self, name, water, size, temperature, country, amount):
        Fish.__init__(self, name, water, size, temperature, country, amount)
        self.set_type("TIBURON")