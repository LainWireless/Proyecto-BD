from funciones import *

PBD = Conectar_BD("localhost","proyect","1234","PBD")

menu = '''MENÚ:
1. Listar nombre de los clientes y cuantos pedidos han hecho.
2. Mostrar el código de los pedidos, junto al nombre del cliente y el nombre del agente cuyo precio del pedido sea igual o mayor al introducido por teclado.
3. Busca nombre de un agente y te muestra cuanto ha ganado por cada pedido que haya conseguido cerrar.
4. Insertar un nuevo cliente en la tabla Clientes.
5. Borra los pedidos realizados que coincidan con el nombre del cliente introducido.
6. Introduce el código de un agente y acto seguido introduce el nuevo porcentaje de comisión que se va a llevar por pedido.
0. Salir.'''

clear()
print(menu)

vopcion = input("\nEscriba el número de la opción para elegirla: ")
try:
    opcion = int(vopcion)
except:
    opcion = 7
    
while opcion != 0:
    if opcion == 1:
        clear()
        listarclientes(PBD)
        contarclientes(PBD)
        input("\nPulse ENTER para volver al menú principal.")
        clear()
    elif opcion == 2:
        clear()
        filtropedidos(PBD)
        input("\nPulse ENTER para volver al menú principal.")
        clear()
    elif opcion == 3:
        clear()
        listaragentes(PBD)
        filtroagente(PBD)
        input("\nPulse ENTER para volver al menú principal.")
        clear()
    elif opcion == 4:
        clear()
        insertarcliente(PBD)
        input("\nPulse ENTER para volver al menú principal.")
        clear()
    elif opcion == 5:
        clear()
        listarclientes(PBD)
        borrarpedido(PBD)
        input("\nPulse ENTER para volver al menú principal.")
        clear()
    elif opcion == 6:
        clear()
        listaragentes(PBD)
        modificaragentes(PBD)
        input("\nPulse ENTER para volver al menú principal.")
        clear()
    else:
        input("\nError. Opción inválida. Pulse ENTER para volver al menú principal.")
        clear()
    
    print(menu)
    vopcion = input("\nEscriba el número de la opción para elegirla: ")
    try:
        opcion = int(vopcion)
    except:
        opcion = 7

Desconectar_BD(PBD)
print("Usted se ha desconectado de la base de datos.")