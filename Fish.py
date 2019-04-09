#Nombre: Fish(Tipo:Class)
#Objetivo: crea objetos tipo Fish con sus propios parametros como lo son Name, Water,
#Size, Temperature, Country y Amount. Sirbe de guia para otras clases
class Fish():
    def __init__(self, name, water, size, temperature, country, amount):
        self.__type = 'PEZ'
        self.__name = name.upper()
        self.__water = water.upper()
        self.__size = size
        self.__temperature = temperature
        self.__country = country.upper()
        self.__amount = amount

    def set_name(self, newName):
        self.__name = newName

    def set_size(self, newSize):
        self.__size = newSize

    def set_temperature(self, nuevaTemp):
        self.__temperature = nuevaTemp

    def set_country(self, newCountry):
        self.__country = newCountry

    def set_amount(self, newAmount):
        self.__amount = newAmount

    def set_type(self, newType):
        self.__type = newType

    def get_name(self):
        return self.__name

    def get_water(self):
        return self.__water

    def get_size(self):
        return self.__size

    def get_temperature(self):
        return self.__temperature

    def get_country(self):
        return self.__country

    def get_type(self):
        return self.__type

    def get_amount(self):
        return self.__amount