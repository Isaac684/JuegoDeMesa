from jugador import jugador
from juego import juego
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


cantidadJuagadores = int(input('Ingrese la cantidad de jugadores (Max:5, Min:2)'))

listJugadores = []

#creacion de jugadores

for i in range(cantidadJuagadores):
    jugadores = jugador(i+1,0,[0,0],False,0,False,False,False)
    listJugadores.append(jugadores)


reglas = juego()

while not reglas.juegoFinalizado:
    for i in range(len(listJugadores)):
        clear_console()
        print(f"Jugador {listJugadores[i].id} va a lanzar los dados")
        print(f"Actualmente te encuentras en la casilla: {listJugadores[i].posicionActual}")
        input("Precione una tecla para lanzarlos...")
        listJugadores[i].lanzamientoInicial()
        if listJugadores[i].salidaMeta:
            listJugadores[i].cambiarPosicion()
            listJugadores = reglas.mecanicaComer(i, listJugadores)
        
        

        while listJugadores[i].tiroDoble:
            input("")
            listJugadores[i].lanzamientoInicial()
            if listJugadores[i].cantidadTirosDobles > 2:
                print(f'El jugador {listJugadores[i].id} a vuelto al inicio porque ha tirado doble tres veces seguida')
                listJugadores[i].cantidadTirosDobles = 0
                listJugadores[i].posicionActual = 1
                listJugadores[i].tiroDoble = False
            else:
                listJugadores[i].cambiarPosicion()
                listJugadores = reglas.mecanicaComer(i, listJugadores)
        input("")

        if listJugadores[i].posicionActual >= 100:
            clear_console()
            print(f"Gana la partida el jugador {listJugadores[i].id}!!!!!")
            reglas.juegoFinalizado = True
            break
        

        

