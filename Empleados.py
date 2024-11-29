from Administrador import Administrador
from Empleado import Empleado
from Recepcionista import Recepcionista

class Empleados:
    def __init__(self):
        self.__empleados = []

    def __nuevo_empleado__(self,empleado):
        self.__empleados.append(empleado)

    def __encontrar_empleado__(self,nick):
        empleado=None

        for e in self.__empleados:
            if e.__get_nick__==nick:
                empleado=e

        return empleado

    def __sumar_consulta__(self,empleado):
        self.__empleados.__getitem__(empleado).__sumar_consulta()