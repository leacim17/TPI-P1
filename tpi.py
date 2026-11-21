def cargar_herramientas(inventario):
    '''Esta función permitirá cargar varias herramientas en una misma operación, indicando el nombre y el stock inicial de cada una.'''

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
    '''Esta función permitirá mostrar el inventario completo de herramientas, indicando el nombre y la cantidad de cada una.'''

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

def main():
    '''Funcion main() para el menu de opciones del sistema de control de inventario.'''

    inventario = [] # Creamos una lista vacia para almacenar los productos del inventario.
    print("===============================")
    print("Sistema de control de inventario")
    print("===============================")
    while True: 
        
        print("Menu de opciones:\n1. Carga de herramientas\n2. Visualizacion de inventario\n3. Consulta de stock\n4. Reporte de agotados\n5. Alta de nuevo producto\n6.Actualizacion de stock(Venta/Ingreso)\n7.Salida del sistema")
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
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    print("Saliendo del sistema...")
                    break
                case _:
                    print("Opcion no valida. Por favor, ingrese una opcion valida.")
        except ValueError as error:
            print(f"!!! Error: {error}. Por favor, ingrese un valor valido.")

main()

