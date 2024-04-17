# Importación de clases desde archivos separados
from jugador import jugador
from juego import juego
from tablero import tablero

# Creación de una instancia de tablero
tabla = tablero()

# Importación del módulo 'os' para limpiar la consola
import os

# Función para limpiar la consola según el sistema operativo
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para validar que el input sea un entero dentro de un rango específico
def validarEntero(datoIngresado):
    while isinstance(datoIngresado, str):  # Mientras el dato ingresado sea una cadena de texto
        try:
            datoIngresado = int(datoIngresado)  # Intenta convertirlo a entero
        except:
            datoIngresado = input('Ingrese solo números enteros\n')  # Si no se puede, pide otro input
        else: 
            if datoIngresado < 2 or datoIngresado > 5:  # Verifica que esté dentro del rango permitido
                datoIngresado = input('La cantidad de jugadores debe ser entre 2 y 5, ingrese un número válido!\n')
            else:
                break  # Si es válido, sale del bucle
    return datoIngresado

# Pedir al usuario la cantidad de jugadores
cantidadJugadores = input('Ingrese la cantidad de jugadores (Max:5, Min:2)\n')
cantidadJugadores = validarEntero(cantidadJugadores)  # Validar que sea un número entero válido

# Crear una lista vacía para almacenar los jugadores
listJugadores = []

# Creación de jugadores y almacenamiento en la lista
for i in range(cantidadJugadores):
    # Crear instancia de jugador y añadirlo a la lista de jugadores
    jugadores = jugador(i + 1, 0, [0, 0], False, 0, False, False)
    listJugadores.append(jugadores)

# Crear una instancia de juego
reglas = juego()

# Bucle principal del juego
while not reglas.juegoFinalizado:
    # Iterar sobre cada jugador en la lista
    for i in range(len(listJugadores)):
        # Limpiar la consola
        clear_console()

        # Mostrar información sobre el turno del jugador actual
        print(f"Jugador {listJugadores[i].id} va a lanzar los dados")
        print(f"Actualmente te encuentras en la casilla: {listJugadores[i].posicionActual}")
        
        # Pedir al jugador que lance los dados o decida salir del juego
        respuesta = input("Presione una tecla para lanzar los dados... o ingrese 'q' para salir.\n")
        
        # Si el jugador decide salir del juego, termina la ejecución
        if respuesta.lower() == 'q':
            exit()

        # Realizar el lanzamiento inicial del jugador y mostrar el tablero
        listJugadores[i].lanzamientoInicial()
        if not listJugadores[i].salidaInicio:
            tabla.mostrarTablero(listJugadores, reglas)

        # Si el jugador ha salido del inicio, aplicar reglas del juego
        if listJugadores[i].salidaInicio:
            listJugadores[i].cambiarPosicion()
            tabla.mostrarTablero(listJugadores, reglas)     
            listJugadores = reglas.casillaPenalizacion(i, listJugadores)
            listJugadores = reglas.casillaTiroDoble(i, listJugadores)
            listJugadores = reglas.mecanicaComer(i, listJugadores)

        # Manejar el caso en el que el jugador obtenga un tiro doble
        while listJugadores[i].tiroDoble:
            input("")
            listJugadores[i].lanzamientoInicial()
            if listJugadores[i].cantidadTirosDobles > 2:
                print(f'El jugador {listJugadores[i].id} ha vuelto al inicio por lanzar doble tres veces seguidas')
                listJugadores[i].cantidadTirosDobles = 0
                listJugadores[i].posicionActual = 0
                listJugadores[i].tiroDoble = False
                tabla.mostrarTablero(listJugadores, reglas)
            else:
                listJugadores[i].cambiarPosicion()
                tabla.mostrarTablero(listJugadores, reglas)
                listJugadores = reglas.casillaPenalizacion(i, listJugadores)
                listJugadores = reglas.casillaTiroDoble(i, listJugadores)
                listJugadores = reglas.mecanicaComer(i, listJugadores)
                
                # Verificar si el jugador ha llegado a la casilla 100
                if listJugadores[i].posicionActual >= 100:
                    clear_console()
                    print(f"Gana la partida el jugador {listJugadores[i].id}!!!!!")
                    reglas.juegoFinalizado = True
                    tabla.mostrarTablero(listJugadores, reglas)
                    input('Saliendo del juego...')     
                    break

        # Reiniciar el indicador de penalización
        listJugadores[i].penalizacion = False

        # Esperar que el jugador presione una tecla para continuar
        input("")

        # Verificar si el jugador ha ganado después de cada turno
        if listJugadores[i].posicionActual >= 100:
            clear_console()
            print(f"Gana la partida el jugador {listJugadores[i].id}!!!!!")
            reglas.juegoFinalizado = True
            tabla.mostrarTablero(listJugadores, reglas)
            input('Saliendo del juego...')     
            break
