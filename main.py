from jugador import jugador
from juego import juego
from tablero import tablero
tabla = tablero()
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def validarEntero(datoIngresado):
    while isinstance(datoIngresado,str):
        try:
            datoIngresado = int(datoIngresado)
        except:
            datoIngresado = input('Ingrese solo numeros enteros\n')
        else: 
            if datoIngresado <2 or datoIngresado > 5:
                datoIngresado = input('La cantidad de jugadores maxima es 5 y la minima 2, ingrese una cantidad valida!\n')
            else:
                break
    return datoIngresado

cantidadJugadores = input('Ingrese la cantidad de jugadores (Max:5, Min:2)\n')
cantidadJugadores = validarEntero(cantidadJugadores)

listJugadores = []

#creacion de jugadores

for i in range(cantidadJugadores):
    jugadores = jugador(i+1,0,[0,0],False,0,False,False)
    listJugadores.append(jugadores)


reglas = juego()

while not reglas.juegoFinalizado:
    for i in range(len(listJugadores)):
        clear_console()
        print(f"Jugador {listJugadores[i].id} va a lanzar los dados")
        print(f"Actualmente te encuentras en la casilla: {listJugadores[i].posicionActual}")
        respuesta = input("Precione una tecla para lanzarlos...")
        if respuesta == 'q' or  respuesta == 'Q':
            quit()

        listJugadores[i].lanzamientoInicial()
        if listJugadores[i].salidaMeta:
            listJugadores[i].cambiarPosicion()
            tabla.mostrarTablero(listJugadores,reglas)     
            listJugadores = reglas.casillaPenalizacion(i,listJugadores)

            listJugadores = reglas.casillaTiroDoble(i,listJugadores)

            listJugadores = reglas.mecanicaComer(i, listJugadores)


        while listJugadores[i].tiroDoble:
            input("")
            listJugadores[i].lanzamientoInicial()
            if listJugadores[i].cantidadTirosDobles > 2:
                print(f'El jugador {listJugadores[i].id} a vuelto al inicio porque ha tirado doble tres veces seguida')
                listJugadores[i].cantidadTirosDobles = 0
                listJugadores[i].posicionActual = 0
                listJugadores[i].tiroDoble = False
            else:
                listJugadores[i].cambiarPosicion()
                tabla.mostrarTablero(listJugadores,reglas)     
                listJugadores = reglas.casillaPenalizacion(i,listJugadores)

                listJugadores = reglas.casillaTiroDoble(i,listJugadores)
        
                listJugadores = reglas.mecanicaComer(i, listJugadores)
                
                if listJugadores[i].posicionActual >= 100:
                    clear_console()
                    print(f"Gana la partida el jugador {listJugadores[i].id}!!!!!")
                    reglas.juegoFinalizado = True
                    break
        listJugadores[i].penalizacion = False

        input("")

        if listJugadores[i].posicionActual >= 100:
            clear_console()
            print(f"Gana la partida el jugador {listJugadores[i].id}!!!!!")
            reglas.juegoFinalizado = True
            break