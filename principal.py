import constantes as cons
import db
from sqlalchemy import text
import pandas as pd

from Administrador import Administrador
from Empleados import Empleados
from Recepcionista import Recepcionista


def conexion ():
    db_config = {
        'dbname': cons.dbname,
        'user': cons.user,
        'password': cons.password,
        'host': cons.host,
        'port': cons.port,
    }
    return db_config

def crearConexion():
    db_config = conexion()
    db_connection = db.PostgreSQLConnection(**db_config)
    db_connection.connect()
    return db_connection

def elegir_cliente():
    try:
        query = text(cons.QUERY_SELECT_ALL_CLIENTE)
        result = db_connection.execute_query(query)
        print("LISTA DE CLIENTES:\n")
        df = pd.DataFrame(result)
        print(df)
        cliente=input("Introduce el id del cliente del que deseas ver los vuelos")
        return cliente

    except Exception as e:
        print("Error, no hay conexion o el id es inválido\n")
        return None

def elegir_usuario():
    try:
        query = text(cons.QUERY_SELECT_ALL_CLIENTE)
        result = db_connection.execute_query(query)
        print("LISTA DE USUARIOS:\n")
        df = pd.DataFrame(result)
        print(df)
        usuario=input("Introduce el id del usuario del que deseas ver la dirección")
        return usuario

    except Exception as e:
        print("Error, no hay conexion o el id es inválido\n")
        return None

def mostrar_vuelos_cliente(id_cliente):
    try:
        query = text(cons.QUERY_SELECT_VUELOS_BY_CLIENTE)
        result = db_connection.execute_query(query,{'id': id_cliente})
        if not result:
            print("No se ha encontrado ningun vuelo para este cliente\n")
        else:
            df = pd.DataFrame(result)
            print(f"VUELOS DEL CLIENTE {id_cliente}:\n")
            print(df)

        return True
    except Exception as e:
        print("Error, no hay conexion o el id es inválido\n")
        return False

def mostrar_direccion_usuario(id_usuario):
    try:
        query = text(cons.QUERY_SELECT_VUELOS_BY_CLIENTE)
        result = db_connection.execute_query(query,{'id': id_usuario})
        print(f"DIRECCIÓN DEL CLIENTE {id_usuario}:\n")
        print(result)

        return True
    except Exception as e:
        print("Error, no hay conexion o el id es inválido\n")
        return False

def comprobarUsuario(empleados,rol):
    nombreUsuario=input("Introduce tu nombre")
    usuarioEncontrado=empleados.__encontrar_empleado__(nombreUsuario)
    if usuarioEncontrado:
        if usuarioEncontrado.__get_rol__()!=rol:
            usuarioEncontrado=None

    return usuarioEncontrado

def vuelosCliente(empleados):
    usuarioValido=comprobarUsuario(empleados,"Recepcionista")

    if usuarioValido:
        cliente=elegir_cliente()

        if cliente:
            if mostrar_vuelos_cliente(cliente):
                empleados.__sumar_consulta__(usuarioValido)

def direccionUsuario(empleados):
    usuarioValido = comprobarUsuario(empleados, "Recepcionista")

    if usuarioValido:
        cliente = elegir_usuario()

        if cliente:
            if mostrar_vuelos_cliente(cliente):
                empleados.__sumar_consulta__(usuarioValido)

def menu():
    empleados = Empleados()
    #añadir aqui a los empleados el admin y el recepcionista
    #cada vez que se realice una actualización o una consulta se deberá sumar 1.
    empleados.__nuevo_empleado__(Administrador("Admin","admin@admin.com"))
    empleados.__nuevo_empleado__(Recepcionista("Recepcionista", "recep@gmail.com"))

    seguir = True

    while seguir:
        print("\n--- MENÚ ---")
        print("1. Mostrar los vuelos de un cliente (no funciona la parte en la que muestra los vuelos)")
        print("2. Mostrar la dirección de un usuario")
        print("3. Vuelo de los pasajeros (no hecho)")
        print("4. Actualización de muertos (no hecho)")
        print("5. Salir")
        opcion=input("Selecciona una opción\n")

        if opcion=="1":
            vuelosCliente(empleados)

        if opcion=="2":
            direccionUsuario(empleados)

        if opcion=="5":
            seguir = False

if __name__ == "__main__":
    db_connection = crearConexion()

    menu()