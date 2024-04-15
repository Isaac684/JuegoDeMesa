from jugador import jugador  # Importa la clase Jugador desde el archivo jugador.py
from juego import juego  # Importa la clase Juego desde el archivo juego.py
from tablero import tablero  # Importa la clase Tablero desde el archivo tablero.py

import colorama
from colorama import Fore, Back, Style  # Importa los estilos de color de la librería Colorama

tabla = tablero()  # Instancia un objeto de la clase Tablero, que sirve para mostrar el tablero del juego
import os

# Función para limpiar la consola
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para validar que el input sea un entero dentro del rango válido
def validarEntero(datoIngresado):
    while isinstance(datoIngresado,str):
        try:
            datoIngresado = int(datoIngresado)
        except:
            datoIngresado = input(Fore.RED+'Ingrese solo numeros enteros\n'+Fore.RESET)
        else: 
            if datoIngresado < 2 or datoIngresado > 5:
                datoIngresado = input(Fore.RED+'La cantidad de jugadores maxima es 5 y la minima 2, ingrese una cantidad valida!\n'+Fore.RESET)
            else:
                break
    return datoIngresado

# Se solicita al usuario que ingrese la cantidad de jugadores y se valida
cantidadJugadores = input('Ingrese la cantidad de jugadores (Max:5, Min:2)\n')
cantidadJugadores = validarEntero(cantidadJugadores)

listJugadores = []  # Lista para almacenar objetos de la clase Jugador

# Creación de jugadores y agregándolos a la lista
for i in range(cantidadJugadores):
    jugadores = jugador(i+1,0,[0,0],False,0,False,False)  # Crea un objeto de la clase Jugador
    listJugadores.append(jugadores)  # Agrega el jugador a la lista de jugadores

reglas = juego()  # Instancia un objeto de la clase Juego

# Bucle principal del juego
while not reglas.juegoFinalizado:
    for i in range(len(listJugadores)):
        clear_console()  # Limpia la consola

        # Muestra el turno del jugador y su posición actual
        print(Style.BRIGHT + f"Jugador {listJugadores[i].id} va a lanzar los dados" + Style.RESET_ALL)
        print(f"Actualmente te encuentras en la casilla: {listJugadores[i].posicionActual}")

        # Espera la entrada del usuario para lanzar los dados o salir del juego
        respuesta = input("Precione una tecla para lanzarlos o 'Q' para salir del juego")

        # Sale del juego si el jugador ingresa 'Q' o 'q'
        if respuesta.lower() == 'q':
            quit()

        # Realiza el lanzamiento inicial del jugador y muestra el tablero si no ha llegado a la meta
        listJugadores[i].lanzamientoInicial()
        if not listJugadores[i].salidaInicio:
            tabla.mostrarTablero(listJugadores, reglas)

        # Realiza las acciones correspondientes si el jugador ha alcanzado la meta
        if listJugadores[i].salidaInicio:
            listJugadores[i].cambiarPosicion()
            tabla.mostrarTablero(listJugadores, reglas)
            listJugadores = reglas.casillaPenalizacion(i, listJugadores)
            listJugadores = reglas.casillaTiroDoble(i, listJugadores)
            listJugadores = reglas.mecanicaComer(i, listJugadores)

        # Bucle para manejar los tiros dobles del jugador
        while listJugadores[i].tiroDoble:
            input("")
            listJugadores[i].lanzamientoInicial()
            if listJugadores[i].cantidadTirosDobles > 2:
                print(f'{Back.RED}El jugador {listJugadores[i].id} a vuelto al inicio porque ha tirado doble tres veces seguida{Back.RESET}')
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
                
                # Verifica si el jugador ha ganado
                if listJugadores[i].posicionActual >= 100:
                    clear_console()
                    print(Back.GREEN+Fore.WHITE+f"Gana la partida el jugador {listJugadores[i].id}!!!!!"+Back.RESET+Fore.RESET)
                    tabla.mostrarTablero(listJugadores, reglas)
                    reglas.juegoFinalizado = True
                    break

        listJugadores[i].penalizacion = False

        input("")

        # Verifica si el jugador ha ganado después de realizar su movimiento
        if listJugadores[i].posicionActual >= 100:
            clear_console()
            print(Back.GREEN+f"Gana la partida el jugador {listJugadores[i].id}!!!!!"+Back.RESET)
            reglas.juegoFinalizado = True
            tabla.mostrarTablero(listJugadores, reglas)
            break
