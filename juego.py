import random as rd
from tablero import tablero
tabla = tablero()
class juego:
    casillasSeguras = [4, 8, 18, 46, 49, 55, 57, 60, 85, 91]
    casillasPenalizacion = [13, 15, 22, 24, 39, 44, 77, 82, 88, 94]
    casillasTirosDoble = [2, 16, 36, 56, 73]
    tunelSeguro = [95, 96, 97, 98, 99]

    meta = 100
    juegoFinalizado = False

    def mecanicaComer(self, posicionJugadorActual, listJugadores):
        for i in range(len(listJugadores)):
            if posicionJugadorActual == i:
                continue
            else:
                if listJugadores[posicionJugadorActual].posicionActual == listJugadores[i].posicionActual:
                    if listJugadores[i].posicionActual in self.casillasSeguras:
                        print(f"El jugador {listJugadores[i].id} se ha salvado de ser comido ya que se encuentra en una casilla segura")
                    elif listJugadores[i].posicionActual in self.tunelSeguro:
                        print(f"El jugador {listJugadores[i].id} se ha salvado de ser comido ya que se encuentra en el tunel seguro")
                        
                    else:
                        print(f"El jugador {listJugadores[posicionJugadorActual].id} ha comido al jugador {listJugadores[i].id}")
                        print(f"Por lo que el jugador {listJugadores[i].id} retrocede 3 casillas!")
                        listJugadores[i].posicionActual -= 3
                        print(f"Se mueve a la casilla: {listJugadores[i].posicionActual}")

                        if listJugadores[posicionJugadorActual].penalizacion == False:
                            print(f"Y el jugador {listJugadores[posicionJugadorActual].id} avanzará 10 casillas!!")

                            listJugadores[posicionJugadorActual].posicionActual += 10
                            print(f"Te mueves a la casilla: {listJugadores[posicionJugadorActual].posicionActual}")
                            self.casillaPenalizacion(posicionJugadorActual,listJugadores)
                        else: 
                            print(f'Debido a que vienes de una casilla de penalizacion, no podras avanzar las 10 casillas adicionales por haber comido al jugador {listJugadores[i].id}')

        return listJugadores
    def casillaPenalizacion(self, posicionActual,listJugadores):
        if listJugadores[posicionActual].posicionActual in self.casillasPenalizacion:
            listJugadores[posicionActual].penalizacion = True
            print(f"\nEl jugador {listJugadores[posicionActual].id} ha caido en una casilla de penalizacion!")
            print(f"Por lo cual se lanzaran los dados para saber cuantas casillas retrocederá")
            input("Preciona una tecla para lanzar los dados...")
            dado1 = rd.randrange(1,6)
            dado2 = rd.randrange(1,6)
            print(f"\nResultado de los dados: Dado 1: {dado1} Dado 2: {dado2}")
            print(f"Por lo que el jugador {listJugadores[posicionActual].id} debera de retroceder {(dado1+dado2)} casillas")
            listJugadores[posicionActual].posicionActual -= (dado1+dado2)
            listJugadores[posicionActual].tiroDoble = False
            print(f"Te mueves a la casilla: {listJugadores[posicionActual].posicionActual}")
            self.casillaPenalizacion(posicionActual,listJugadores)
            #self.casillaTiroDoble(posicionActual,listJugadores)
            self.mecanicaComer(posicionActual,listJugadores)
        return listJugadores

        
        

    def casillaTiroDoble(self, posicionJugadorActual, listJugadores):

        if listJugadores[posicionJugadorActual].posicionActual in self.casillasTirosDoble:
            print(f'El jugador {listJugadores[posicionJugadorActual].id} ha caido en una casilla de bonificacion de tiro doble, por lo tanto volvera a tirar')
            input()
            listJugadores[posicionJugadorActual].lanzamientoDeBonificacion()
            self.casillaPenalizacion(posicionJugadorActual,listJugadores)
            self.mecanicaComer(posicionJugadorActual,listJugadores)
            return listJugadores
        else:
            return listJugadores
            