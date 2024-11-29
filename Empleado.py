class Empleado:
    def __init__(self,nick,correo):
        self.__nick=nick
        self.__correo=correo
        self.__rol="Empleado"

    def __get_nick__(self):
        return self.__nick

    def __get_rol__(self):
        return self.__rol