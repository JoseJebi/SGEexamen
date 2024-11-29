from Empleado import Empleado

class Recepcionista(Empleado):
    def __init__(self, nick, correo):
        super().__init__(nick, correo)
        self.__num_consultas=0
        self.__rol = "Recepcionista"

    def __sumar_consulta(self):
        self.__num_consultas+=1