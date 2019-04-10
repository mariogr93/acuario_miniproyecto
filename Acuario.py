
from Fish import Fish
from Shark import Shark
from Turtle import Turtle


#Nombre: Aquarium(Tipo:Class)
#Objetivo: crea objetos tipo Aquarium el cual almacena, modifica y muestra informacion de una tabla hash propia de la clase
class Aquarium():
    def __init__(self):
        self.__list = [[],[],[],[],[],[],[],[],[],[]]


    def start(self):
        print 'OPCIONES: \na)Crear\nb)Buscar\nc)Modificar\nd)Eliminar'
        opciones = raw_input('Que desea hacer? (a,b,c,d) ').upper()
        result = None
        if opciones == 'A':
            result = self.create()
        if opciones == 'B':
            result =  self.show()
        if opciones == 'C':
            result = self.modifyName()

        if opciones == 'D':
            result = self.delete()
        else:
            result = self.start()
        return result


    def create(self):
        print 'OPCIONES: \na)Pez\n)bTiburon\nc)Tortuga'
        opciones = raw_input('Que desea hacer? (a,b,c) ').upper()
        name = raw_input('Nombre del animal: ').upper()
        water = raw_input('Tipo de Agua: ').upper()
        size = raw_input('Tamano en CM (solo numeros): ')
        temperature = raw_input('Temperatura ideal del ambiente(solo numeros y grados centigrados): ')
        country = raw_input('Pais de procedencia: ').upper()
        amount = raw_input('Cantidad a registrar: ').upper()
        if self.stringTest(name) == False or self.stringTest(water) == False or self.stringTest(country) == False \
                or self.integerTest(size) == False or self.integerTest(temperature) == False or self.integerTest(
            amount) == False:
            print 'Formato de Informacion Incorrecto, intente nuevamente'
            return self.create()
        if opciones == 'A':
            animal = Fish(name, water, size, temperature, country, amount)
        if opciones == 'B':
            animal = Shark(name, water, size, temperature, country, amount)
        if opciones == 'C':
            animal = Turtle(name, water, size, temperature, country, amount)

        return self.register(animal), self.start()

# Nombre: hashCode
# Parametros: animal(Tipo: Fish, Shark, Turtle)
# Objetivo: utiliza el metodo get_name propio del objeto para utilizar el nombre del animal y asignarle una posicion en la tabla Hash .
# Retorno: retorna la posicion donde se almacenara el objeto.
    def hashCode(self, word):
        total = 0
        for letter in word:
            total = (total + ord(letter))%10
        return total

# Nombre: register
# Parametros: animal(Tipo: Fish, Shark, Turtle)
# Objetivo: Registrar el objeto Animal en el la tabla Hash __list de acuerdo al resultado del metodo hashCode.
# Retorno: dependiendo de la evaluacion, el metodo retorna donde hay un error o si el registro fue exitoso o cancelado.
    def register(self, animal):
        if self.evaluation(animal) == True:
            self.__list[self.hashCode(animal.get_name())].append([animal.get_name(), animal])
            print '.......................\nRegistro Completo\n.......................'
        else:
            print 'Error en el registro del animal ' + animal.get_name()

# Nombre: delete
# Parametros: animal(Tipo: Fish, Shark, Turtle)
# Objetivo: Elimina el objeto Animal en el la tabla Hash __list.
# Retorno: None
    def delete(self):
        name = raw_input('Nombre ').upper()
        counter = 0
        bucket = self.hashCode(name)
        for element in self.get_list()[bucket]:
            if name in element:
                self.get_list()[bucket].pop(counter)
                print '.......................\nNombre Eliminado\n.......................'

            else:
                counter +=1
        return self.start()



# Nombre: modifyName
# Parametros: Animal(Tipo: Fish, Shark, Turtle)
# Objetivo: Modificar el nombre del Objeto (Fish, Shark, Turtle) y modificar su registro en la tabla hash.
# Retorno: dependiendo de la evaluacion, el metodo retorna donde hay un error o si el registro fue exitoso o cancelado.
    def modifyName(self):
        name = raw_input('Digite el Nombre del animal que desea Modificar: ').upper()
        bucket = self.hashCode(name)
        counter = 0
        animal =[]
        if self.stringTest(name) == True:
            for element in self.get_list()[bucket]:
                if name in element:
                    animal.append(self.__list[bucket][counter].pop())
                counter +=1

            if len(animal)> 0:
                newName = raw_input('Digite el nuevo nombre ').upper()
                animal[0].set_name(newName)
                self.register(animal[0])

                print '.......................\nModificacion Completa\n.......................'
                self.start()
            else:
                print 'Animal no encontrado, intente nuevamente'
                self.modifyName()
        else:
            print 'El nuevo nombre tiene caracteres inadecuados'
            self.modifyName()




# Nombre: modifySize
# Parametros: Animal(Tipo: Fish, Shark, Turtle).
# Objetivo: Modifica el tamano del objeto (Fish, Shark, Turtle).
# Retorno: dependiendo de la evaluacion, el metodo retorna donde hay un error o si el registro fue exitoso o cancelado.
    def modifySize(self,animal):
        newSize = raw_input('Digite el nuevo tamano ')
        if self.integerTest(newSize) == True:
            animal.set_size(newSize)
            print 'Cambio Completado'
        else:
            print 'El tamano solo puede recibir numeros como informacion, por favor intente nueva mente'
            self.modifySize(animal)

# Nombre: findWName
# Parametros: None
# Objetivo: Utiliza la funcion raw_imput para recibir el nombre que se desea buscar y junto
# con el metodo hashCode lo utiliza para buscar en la tabla Hash la informacion guardada con dicho nombre.
# Retorno: Retorna el Objeto guardado  en una nueva lista o se llama de nuevo de manera recursiva en caso de algun error.
    def findWName(self):
        name = raw_input('Digite el Nombre del animal que desea buscar: ').upper()
        animal = []
        bucket = self.hashCode(name)
        counter = 0
        if self.stringTest(name) == True:
            for element in self.get_list()[bucket]:
                if name in element:
                    animal.append(self.__list[bucket][counter][1])
                counter +=1
        else:
            print 'Animal no esta registrado o el nombre fue escrito incorrectamente'
            self.findWName()
        return animal

# Nombre: findWType
# Parametros: None
# Objetivo: Utiliza la funcion raw_imput para recibir el tipo de animal que se desea buscar y lo utiliza
# para buscar en la tabla Hash  a todos los animales pertenecientes a ese tipo.
# Retorno: Retorna el Objeto guardado  en una nueva lista o se llama de nuevo de manera recursiva en caso de algun error.
    def findWType(self):
        type = raw_input('Digite el Tipo de animales que desea buscar: ').upper()
        animals = []
        counter = 0
        if self.stringTest(type) == True:
            while counter < 10:
                for element in self.get_list()[counter]:
                    if len(element) > 1:
                        if element[1].get_type() == type:
                            animals.append(element[1])
                counter +=1
        return animals
#Nombre: show
#Parametros: None
#Objetivo: Mostrar la informacion que findWName y findWType recopilan.
#Retorno: Imprime la informacion de los objetos que se le suministren en una lista mediante findWName y findWType.
    def show(self):
        print 'OPCIONES\na)Por Nombre\nb)Por Tipo'
        how = raw_input('Como desea realizar la busqueda? (a,b) ').upper()
        if how == 'A':
            animal = self.findWName()
        if how == 'B':
            animal = self.findWType()

        for element in animal:
            print ['Nombre: ' + element.get_name(),'Tipo de animal: ' + element.get_type(),
                     'De agua: ' + element.get_water(),'Tamano aproximado de: ' + element.get_size(),
                      'Temperatura recomendable: ' + element.get_temperature(), 'Pais nativo: ' + element.get_country(),
                      'Cantidad en tanque: ' + element.get_amount()]

# Nombre: intergerTest
# Parametros: interger(Tipo: Str)
# Objetivo: evaluar el parametro "interger" y asegurar de que solo sean numeros sus caracteres.
# Retorno: retorna True o False
    def integerTest(self, string):
        result = True
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        evaluate = string.upper()
        for element in evaluate:
            if element not in numbers:
                result = False
        return result

# Nombre: stringTest
# Parametros: string(Tipo: Str)
# Objetivo:evaluar el parametro "string" y asegurar de que sean solo letras sus caracteres.
# Retorno: retorna True o False
    def stringTest(self, string):
        result = True
        letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', ' ']
        evaluate = string.upper()
        for element in evaluate:
            if element not in letters:
                result = False
        return result

# Nombre: evaluation
# Parametros: animal(Tipo: Fish, Shark, Turtle)
# Objetivo: Evaluar toda la informacion que se desea registrar y que no tenga caracteres inadecuados.
# Retorno: True o False
    def evaluation(self, animal):
        result = True
        letters = [animal.get_name(), animal.get_water(), animal.get_country()]
        numbers = [animal.get_size(), animal.get_temperature(), animal.get_amount()]
        for element in letters:
            if self.stringTest(element) != True:
                result = False
        for element in numbers:
            if self.integerTest(element) != True:
                result = False
        return result

# Nombre:get_list
# Parametros: None
# Objetivo: retornar la lista Hash de la clase acuario
# Retorno: __list
    def get_list(self):
        return self.__list



acu = Aquarium()
print acu.start()
