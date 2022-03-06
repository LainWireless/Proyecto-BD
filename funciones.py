import sys
import MySQLdb
import os

def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

def Conectar_BD(host,usuario,password,nombrebd):
    try:
        db = MySQLdb.connect(host,usuario,password,nombrebd)
        return db
    except MySQLdb.Error as e:
        print("ERROR. No se pudo conectar a la base de datos:",e)
        sys.exit(1)
        
def Desconectar_BD(db):
    db.close()

def listarclientes(db):
    sql="SELECT NOMBRE FROM CLIENTES"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        clientes = cursor.fetchall()
        print("Clientes:")
        for cliente in clientes:
            print("\nNombre:",cliente["NOMBRE"])
    except:
        print("Error en la consulta.")

def contarclientes(db):
    sql="SELECT NOMBRE FROM CLIENTES"
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        print("\nNúmero de clientes:", cursor.rowcount)
    except:
        print("Error en la consulta.")

def filtropedidos(db):
    filtro=input("Introduzca precio del pedido: ")
    sql=f"SELECT NUM_PEDIDO, c.NOMBRE, a.NOMBRE FROM PEDIDOS, c CLIENTES, a AGENTES WHERE PRECIO_PEDIDO>=%d ORDER BY NUM_PEDIDO"%filtro
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        pedidos = cursor.fetchall()
        if cursor.rowcount != 0:
            print(f"\nPedidos cuyo precio es igual o mayor a {filtro}:")
            for pedido in pedidos:
                print("\nPedido:",pedido["NUM_PEDIDO"],"\nCliente:",pedido["c.NOMBRE"],"\nAgente:",pedido["a.NOMBRE"])
        else:
            input("\nNo se han encontrado precios iguales o mayores al que deseaba buscar.")
    except:
        print("Error en la consulta.")

def filtroagente(db):
    filtro=input("Introduzca el nombre del agente: ")
    sql=f"SELECT NUM_PEDIDO, PRECIO_PEDIDO, COMISION*PRECIO_PEDIDO FROM AGENTES,PEDIDOS WHERE CODIGO=CODIGO_AGENTE IN (SELECT CODIGO FROM AGENTES WHERE NOMBRE = '{filtro}')"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        ganancias = cursor.fetchall()
        if cursor.rowcount != 0:
            print(f"\nAgente {filtro}:")
            for ganancia in ganancias:
                print("\nPedido:",ganancia["NUM_PEDIDO"],"\nPrecio:",ganancia["PRECIO_PEDIDO"],"\nGanancias:",ganancia["COMISION*PRECIO_PEDIDO"])
        else:
            input("\nNo se han encontrado coincidencias con su búsqueda.")
    except:
        print("Error en la consulta.")

def insertarcliente(db):
    cod_cliente=input("Introduzca el código del nuevo cliente, puede ser alfanumérico: ")
    nombre_cliente=input("Introduzca el nombre del nuevo cliente: ")
    ciudad_cliente=input("Introduzca la ciudad del nuevo cliente: ")
    area_cliente=input("Introduzca el area de trabajo del nuevo cliente, debe ser una ciudad: ")
    pais_cliente=input("Introduzca el pais del nuevo cliente: ")
    nivel_cliente=input("Introduzca el nivel del nuevo cliente, debe ser un número de una sola cifra: ")
    Tel_cliente=input("Introduzca el número de teléfono del nuevo cliente: ")
    cod_agente_cliente=input("Introduzca el código del agente del nuevo cliente, puede ser alfanumérico y debe de existir: ")
    sql=f"INSERT INTO CLIENTES values ('{cod_cliente}','{nombre_cliente}','{ciudad_cliente}','{area_cliente}','{pais_cliente}','{nivel_cliente}','{Tel_cliente}','{cod_agente_cliente}')"
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        input("\Cliente nuevo agregado.")
    except:
        print("Error en la consulta.")
        db.rollback()

def borrarpedido(db):
    filtro=input("\nIntroduzca el nombre del cliente del cual desea eliminar sus pedidos: ")
    sql=f"DELETE FROM PEDIDOS WHERE CODIGO_CLIENTE IN (SELECT CODIGO FROM CLIENTES WHERE NOMBRE = '{filtro}')"
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        input(f"\nPedidos del cliente {filtro} eliminados.")
    except:
        print("Error en la consulta.")
        db.rollback()

def modificaragentes(db):
    filtro=input("\nIntroduzca el código del agente para modificar su comisión: ")
    nueva_comision=input("\nIntroduzca la nueva comisión para el agente seleccionado: ")
    sql=f"UPDATE AGENTES SET COMISION = {nueva_comision} WHERE CODIGO = '{filtro}'"
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        input(f"\nComisión del agente {filtro} actualizada.")
    except:
        print("Error en la consulta.")
        db.rollback()
        
def listaragentes(db):
    sql="SELECT CODIGO,NOMBRE FROM AGENTES"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        agentes = cursor.fetchall()
        print("Agentes:")
        for agente in agentes:
            print("\nCódigo:",agente["CODIGO"],"\nNombre:",agente["NOMBRE"])
    except:
        print("Error en la consulta.")