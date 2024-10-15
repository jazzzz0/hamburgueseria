# Importaciones
import sqlite3
from time import asctime


# Funciones
def ingreso_combo(combo):
    match combo:
        case "S":
            mensaje = "Combo S"
        case "D":
            mensaje = "Combo D"
        case "T":
            mensaje = "Combo T"
        case "F":
            mensaje = "Flurby"
        case _:
            mensaje = "NO ENCONTRADO"

    while True:
        variable_combo = input(f"Ingrese cantidad de {mensaje}: ")
        try:
            variable_combo = int(variable_combo)
            break
        except ValueError:
            print("La cantidad debe ser numérica.")

    return variable_combo


# Función para ingresar encargado
def ingreso_encargado():
    mensaje_bienvenida = "Bienvenido a Hamburguesas IT\nIngrese su nombre encargado: "
    nombre = input(mensaje_bienvenida)
    while not nombre.strip():
        print("El nombre no puede estar vacío.")
        nombre = input(mensaje_bienvenida)
    return nombre.title()


# Función que inserta la venta en la tabla Ventas de la base de datos
def insertar_venta_db(venta):
    cursor = conexion.cursor()
    try:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS venta (id INTEGER PRIMARY KEY, cliente TEXT, fecha TEXT, combo_S INTEGER, combo_D INTEGER, combo_T INTEGER, flurby INTEGER, total REAL)"
        )
        conexion.commit()
    except sqlite3.OperationalError as e:
        print(f"ERROR. {e}")

    try:
        cursor.execute(
            f"INSERT INTO venta (cliente, fecha, combo_S, combo_D, combo_T, flurby, total) VALUES (?,?,?,?,?,?,?)",
            (
                venta["cliente"],
                venta["fecha"],
                venta["combo_s"],
                venta["combo_d"],
                venta["combo_t"],
                venta["flurby"],
                venta["total"],
            ),
        )
        conexion.commit()
        print("Venta confirmada")
    except sqlite3.OperationalError as e:
        print(f"ERROR. {e}")


# Función que inserta el registro de turnos de encargado
def insertar_registro_db(encargado, evento):
    cursor = conexion.cursor()
    try:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS registro (id INTEGER PRIMARY KEY, encargado TEXT, fecha TEXT, evento TEXT, caja REAL)"
        )
        conexion.commit()
    except sqlite3.OperationalError as e:
        print(f"ERROR. {e}")

    try:
        cursor.execute(
            f"INSERT INTO registro (encargado, fecha, evento, caja) VALUES (?,?,?,?)",
            (encargado, asctime(), evento, caja),
        )
        conexion.commit()
    except sqlite3.OperationalError as e:
        print(f"ERROR. {e}")


# Función para hacer un pedido nuevo
def nuevo_pedido():
    precio_S, precio_D, precio_T, precio_Flurby = 5, 6, 7, 2
    # Ingreso nombre del cliente
    nombre_cliente = input("Ingrese nombre del cliente: ")
    while not nombre_cliente.strip():
        print("El nombre no puede estar vacío.")
        nombre_cliente = input("Ingrese nombre del cliente: ")

    # Ingreso combo Simple
    cant_combo_s = ingreso_combo("S")

    # Ingreso combo Doble
    cant_combo_d = ingreso_combo("D")

    # Ingreso combo Triple
    cant_combo_t = ingreso_combo("T")

    # Ingreso Flurby
    cant_flurby = ingreso_combo("F")

    # Calcula precio total
    precio_total = (
        (cant_combo_s * precio_S)
        + (cant_combo_d * precio_D)
        + (cant_combo_t * precio_T)
        + (cant_flurby * precio_Flurby)
    )
    print(f"Total ${precio_total}")

    # Ingreso abono cliente
    while True:
        pago = input("Abona con $ ")
        try:
            pago = float(pago)
            if pago < precio_total:
                print("Pago insuficiente.")
                continue
            break
        except ValueError:
            print("El pago debe ser numérico.")

    # Calcula vuelto
    vuelto = pago - precio_total
    print(f"Vuelto $ {round(vuelto, 2)}")

    # Confirmar pedido
    while True:
        confirmacion = input("¿Confirma pedido? (y/n): ")
        if confirmacion.lower() == "y":
            venta = {
                "cliente": nombre_cliente,
                "fecha": asctime(),
                "combo_s": cant_combo_s,
                "combo_d": cant_combo_d,
                "combo_t": cant_combo_t,
                "flurby": cant_flurby,
                "total": precio_total,
            }
            insertar_venta_db(venta)
            global caja
            caja += precio_total
            break
        elif confirmacion.lower() == "n":
            print("Pedido cancelado")
            break
        else:
            print("Respuesta no válida.")


# Programa principal
global conexion
conexion = sqlite3.connect("comercio.sqlite")

caja = 0

nombre = ingreso_encargado()
insertar_registro_db(nombre, "IN")
while True:
    menu = f"Hamburguesas IT\nEncargad@ -> {nombre}\nRecuerda, siempre hay que recibir al cliente con una sonrisa :)\n1. Ingreso nuevo pedido\n2. Cambio de turno\n3. Apagar sistema\n>>> "
    opcion_seleccionada = input(menu)
    match opcion_seleccionada:
        case "1":
            # 1. Ingresar nuevo pedido
            nuevo_pedido()
        case "2":
            # 2. Cambio de turno
            insertar_registro_db(nombre, "OUT")
            caja = 0
            nombre = ingreso_encargado()
            insertar_registro_db(nombre, "IN")
        case "3":
            # 3. Apagar sistema
            break
        case _:
            # Default
            print("\nOpción no válida.\n")
            continue

conexion.close()
print("Sistema apagado.")
