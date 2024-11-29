from Empleado import Empleado
class Administrador(Empleado):
    def __init__(self, nick, correo):
        super().__init__(nick, correo)
        self.__num_actualizaciones=0
        self.__rol = "Administrador"