from idlelib.query import Query

dbname = 'postgres'
user = 'postgres'
password = 'root'
host = 'localhost'
port = '5432'

#obtener todos los clientes que tenemos
QUERY_SELECT_ALL_CLIENTE = 'SELECT p.id, p.nombre, p.apellidos FROM scexamen."UsuariosVuelo" uv JOIN scexamen."Personas" p on uv.idPasajero=p.id'

#obtener los vuelos de un cliente
QUERY_SELECT_VUELOS_BY_CLIENTE = 'SELECT (SELECT c.nombre FROM scexamen."Ciudades" c JOIN scexamen."Vuelos" v on c.) FROM scexamen."Vuelos" v JOIN scexamen."UsuariosVuelo" uv'

#obtener la dirección de un usuario
QUERY_SELECT_DIRECCION_USUARIO = 'SELECT d.calle FROM scexamen."Direcciones" d JOIN scexamen."Personas" p on d.id=p.iddireccion WHERE p.id = :id;'


#sacar las ventas de de x clientes
QUERY_SELECT_VENTAS_BY_CLIENTE = 'SELECT id, fecha_venta, impuesto FROM public."venta" WHERE id_cliente = :id;'
#sacar los productos de una venta de x cliente
QUERY_SELECT_PRODUCTOS_BY_CLIENTE = 'SELECT * FROM public."producto" WHERE id IN (SELECT id_prod FROM public."producto_venta" WHERE id_venta IN (SELECT id FROM public."venta" WHERE id_cliente = :id));'

#Realizar el calculo de la venta numero 8 el precio total sin impuestos, los impuestos pagados y el precio total con impuestos.
QUERY_SELECT_VENTA_IMPUESTO = 'select p.precio, pv.cantidad, v.impuesto from public."producto" as p join public."producto_venta" as pv on p.id=pv.id_prod join public."venta" as v on pv.id_venta=v.id where id_venta = 8;'