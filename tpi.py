def cargar_herramientas(inventario):
    '''Esta función permite cargar varias herramientas en una misma operación, indicando el nombre y el stock inicial de cada una.'''

    ## while True para que el usuario pueda ingresar la cantidad de herramientas que desea cargar, y si ingresa un valor no valido, se le pedira que ingrese nuevamente el valor.
    while True:
        ## try/except para controlar los errores del usuario al ingresar la cantidad de herramientas que quiere cargar
        try: 
            cantidad_herramientas = int(input("Ingrese la cantidad de herramientas a cargar: "))
            if cantidad_herramientas <= 0:
                raise ValueError("La cantidad de herramientas debe ser un número positivo.")
            break
        except ValueError as error:
            print(f"!!! Error: {error}. Por favor, ingrese un valor valido.")

    ## Creamos un bucle while para que el usuario pueda ingresar los datos de cada herramienta, y si ingresa un valor no valido, se le pedira que ingrese nuevamente el valor.
    i = 0
    while i < cantidad_herramientas: 
        ## try/except para controlar los errores del usuario al ingresar el nombre de la herramienta.
        while True:
            try: 
                nombre_herramienta = input(f"Ingrese el nombre de la herramienta N°{i+1}: ")
                nombre_herramienta = nombre_herramienta.strip()  # Eliminamos espacios en blanco al inicio y al final. Ademas si el usuario ingresa solo espacios en blanco, se considera como un nombre vacio ya que strip() devuelve una cadena vacia.
                if not nombre_herramienta:
                    raise ValueError("El nombre de la herramienta no puede estar vacío")
                for herramienta in inventario:
                    if herramienta['herramienta'].lower() == nombre_herramienta.lower():
                        raise ValueError("La herramienta ya existe en el inventario")
                break
            except ValueError as error:
                print(f"!!! Error: {error}. Por favor, ingrese un valor valido.")

        ## try/except para controlar los errores del usuario al ingresar el stock inicial de la herramienta.
        while True:
            try: 
                stock_inicial = int(input(f"Ingrese el stock inicial de la herramienta N°{i+1}: "))
                if stock_inicial < 0:
                    raise ValueError("El stock inicial debe ser un número entero no negativo.")
                break
            except ValueError as error:
                print(f"!!! Error: {error}. Por favor, ingrese un valor valido.")
        

        inventario.append({'herramienta': nombre_herramienta, 'cantidad': stock_inicial}) # Agregamos la herramienta al inventario como un diccionario con las claves 'herramienta' y 'cantidad'.
        print("======")
        print(f"Herramienta '{nombre_herramienta}' con stock inicial de {stock_inicial} agregada al inventario.")
        print("======")

        i += 1  # incrementamos el contador una vez que la herramienta fue validada y agregada correctamente al inventario.

def mostrar_inventario(inventario):
    '''Esta función permite mostrar el inventario completo de herramientas, indicando el nombre y la cantidad de cada una.'''

    ## Verificamos si la lista inventario está vacía.
    ## Si no contiene elementos, se informa al usuario y se finaliza la función con return.
    if not inventario:
        print("==========================")
        print("El inventario está vacío.")
        print("==========================")
        return
    

    print("Inventario de herramientas:")
    print("==========================")
    print('''Herramienta\t|\tStock''')
    print("-------------------------------")
    ## Recorremos la lista inventario mediante un ciclo for.
    ## En cada iteración, la variable herramienta representa uno de los diccionarios.
    for herramienta in inventario:
        print(f"{herramienta['herramienta']}\t|\t{herramienta['cantidad']}") # Accedemos a las claves del diccionario para mostrar el nombre y la cantidad.
        print("-------------------------------")
    print("==========================")

def consultar_stock(inventario):
    '''Esta función permite consultar el stock disponible de una herramienta específica.'''

    ## Verificamos si la lista inventario está vacía.
    if not inventario:
        print("==========================")
        print("El inventario está vacío.")
        print("==========================")
        return

    nombre_herramienta = input("Ingrese el nombre de la herramienta a consultar: ")
    nombre_herramienta = nombre_herramienta.strip() # Eliminamos los espacios en blanco al principio y al final.

    # Validamos que el nombre ingresado no esté vacío.
    if not nombre_herramienta:
        raise ValueError("El nombre de la herramienta no puede estar vacío.") # Si está vacío, lanzamos un ValueError que será capturado por main().

    for herramienta in inventario:
        if herramienta['herramienta'].lower() == nombre_herramienta.lower(): # Comparamos los nombres utilizando lower() para ignorar diferencias
            print(f"Stock de '{nombre_herramienta}': {herramienta['cantidad']}")
            return

    ## Si finaliza el recorrido sin encontrar coincidencias, informamos al usuario.
    print(f"La herramienta '{nombre_herramienta}' no se encuentra en el inventario.")

def reporte_agotados(inventario):
    '''Esta función permite generar un reporte de las herramientas que se encuentran agotadas (stock = 0).'''

    ## Verificamos si la lista inventario está vacía.
    if not inventario:
        print("==========================")
        print("El inventario está vacío.")
        print("==========================")
        return

    print("Reporte de herramientas agotadas:")
    print("==========================")
    # Inicializamos una variable testigo en False. Cambia a True si encontramos alguna herramienta agotada.
    hay_agotados = False
    ## Recorremos el inventario para identificar las herramientas sin stock.
    for herramienta in inventario:
        if herramienta['cantidad'] == 0:
            print(f"Herramienta: {herramienta['herramienta']}")
            print("--------------------------")
            hay_agotados = True

    ## Si el testigo sigue en False, significa que no encontramos agotados.
    if not hay_agotados:
        print("¡Felicidades! No hay productos agotados.")

def alta_producto(inventario):
    '''Esta función permite incorporar una nueva herramienta al inventario, indicando su nombre y stock inicial.'''

    nombre_herramienta = input("Ingrese el nombre de la herramienta: ")
    nombre_herramienta = nombre_herramienta.strip()  # Eliminamos espacios en blanco al inicio y al final. Ademas si el usuario ingresa solo espacios en blanco, se considera como un nombre vacio ya que strip() devuelve una cadena vacia.
    if not nombre_herramienta:
        raise ValueError("El nombre de la herramienta no puede estar vacío")
    for herramienta in inventario:
        if herramienta['herramienta'].lower() == nombre_herramienta.lower():
            raise ValueError("La herramienta ya existe en el inventario")

    stock_inicial = int(input("Ingrese el stock inicial de la herramienta: "))
    if stock_inicial < 0:
        raise ValueError("El stock inicial debe ser un número entero no negativo.")

    inventario.append({'herramienta': nombre_herramienta, 'cantidad': stock_inicial}) # Agregamos la herramienta al inventario como un diccionario con las claves 'herramienta' y 'cantidad'.
    print("======")
    print(f"Herramienta '{nombre_herramienta}' con stock inicial de {stock_inicial} agregada al inventario.")
    print("======")

def actualizar_stock(inventario):
    '''Esta funcion permite registrar una venta o un nuevo ingreso de herramientas ya registradas modificando el inventario'''
    ## Verificamos si la lista inventario está vacía.
    if not inventario:
        print("==========================")
        print("El inventario está vacío.")
        print("==========================")
        return

    nombre_herramienta = input("Ingrese el nombre de la herramienta: ")
    nombre_herramienta = nombre_herramienta.strip()  # Eliminamos espacios en blanco al inicio y al final. Ademas si el usuario ingresa solo espacios en blanco, se considera como un nombre vacio ya que strip() devuelve una cadena vacia.
    if not nombre_herramienta:
        print("La herramienta ingresada no se encontro en el inventario")
        return

    herramienta_encontrada = False
    for herramienta in inventario:
        if herramienta['herramienta'].lower() == nombre_herramienta.lower():
            herramienta_encontrada = True
            print("1. Venta\n2. Ingreso")
            tipo_movimiento = input("Ingrese el tipo de moviemiento que quiere realizar: ").strip().lower()
            if tipo_movimiento == '1' or tipo_movimiento == 'venta':
                cantidad_venta = int(input(f"¿Cuantos/as {herramienta['herramienta']} quiere vender?: "))
                if cantidad_venta <= 0:
                    raise ValueError("La cantidad de ventas debe ser un entero positivo")
                if cantidad_venta > herramienta['cantidad']:
                    raise ValueError("No cuenta con el stock necesario para realizar la venta.")

                herramienta['cantidad'] = herramienta['cantidad'] - cantidad_venta

                print(f"El stock de {herramienta['herramienta']} ya fue modificado. Stock actual: {herramienta['cantidad']}.")
                return 
                
            elif tipo_movimiento == '2' or tipo_movimiento == 'ingreso':
                cantidad_ingreso = int(input(f"¿Cuantos/as {herramienta['herramienta']} quiere ingresar?: "))
                if cantidad_ingreso <= 0:
                    raise ValueError("La cantidad de ingresos debe ser un entero positivo")
                herramienta['cantidad'] = herramienta['cantidad'] + cantidad_ingreso

                print(f"El stock de {herramienta['herramienta']} ya fue modificado. Stock actual: {herramienta['cantidad']}.")
                return 
            else: 
                print("La opcion de operacion seleccionada es invalida.")
                return 
        
    if not herramienta_encontrada:
        raise ValueError("La herramienta no existe en el inventario")
    

def main():
    '''Funcion main() para el menu de opciones del sistema de control de inventario.'''

    inventario = [] # Creamos una lista vacia para almacenar los productos del inventario.
    print("===============================")
    print("Sistema de control de inventario")
    print("===============================")
    while True: 
        
        print("Menu de opciones:\n1. Carga de herramientas\n2. Visualizacion de inventario\n3. Consulta de stock\n4. Reporte de agotados\n5. Alta de nuevo producto\n6. Actualizacion de stock (Venta/Ingreso)\n7. Salida del sistema")
        ## try/except para controlar los errores del usuario al ingresar la opcion del menu elegida. 
        try: 
            ## usamos match para no realizar una concatenacion de if/else y que sea mas legible el codigo.
            opcion = int(input("Ingrese la opcion deseada: "))
            if opcion < 1 or opcion > 7:
                raise ValueError("La opcion ingresada no se encuentra dentro del rango permitido (1-7)")
            match opcion:
                case 1:
                    cargar_herramientas(inventario) ## MM: Esta OK
                case 2:
                    mostrar_inventario(inventario) ## MM: Esta OK
                case 3:
                    consultar_stock(inventario) ## MM: Esta OK
                case 4: 
                    reporte_agotados(inventario) ## MM: Esta OK
                case 5:
                    alta_producto(inventario)
                case 6:
                    actualizar_stock(inventario)
                case 7:
                    print("Saliendo del sistema...")
                    return

        except ValueError as error:
            print(f"!!! Error: {error}. Por favor, ingrese un valor valido.")

main()

