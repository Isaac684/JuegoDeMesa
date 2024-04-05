import random as rd
class juego:
    casillasSeguras = [57,46,4,49,91,18,8,55,85,60]
    casillasPenalizacion = [13,88,87,15,82,22,77,44,39,24]
    casillasTirosDoble = [36,73,2,56,16]
    tunelSeguro = [95,96,97,98,99]
    meta = 100
    juegoFinalizado = False

    def mecanicaComer(self, posicionJugadorActual, listJugadores):
        for i in range(len(listJugadores)):
            if posicionJugadorActual == i:
                continue
            else:
                if listJugadores[posicionJugadorActual].posicionActual == listJugadores[i].posicionActual:
                    if listJugadores[i].posicionActual in self.casillasSeguras or listJugadores[i].posicionActual in self.tunelSeguro:
                        print(f"El jugador {listJugadores[i].id} se ha salvado de ser comido ya que se encuentra en una casilla segura")
                    else:
                        print(f"El jugador {listJugadores[posicionJugadorActual].id} ha comido al jugador {listJugadores[i].id}")
                        print(f"Por lo que el jugador {listJugadores[i].id} retrocede 3 casillas!")
                        print(f"Y el jugador {listJugadores[posicionJugadorActual].id} avanzará 10 casillas!!")
                        listJugadores[i].posicionActual -= 3
                        listJugadores[posicionJugadorActual].posicionActual += 10
                        self.casillaPenalizacion(posicionJugadorActual,listJugadores)

        return listJugadores
    def casillaPenalizacion(self, posicionActual,listJugadores):
        if listJugadores[posicionActual].posicionActual in self.casillasPenalizacion:
            print(f"El jugador {listJugadores[posicionActual].id} ha caido en una casilla de penalizacion!")
            print(f"Por lo cual se lanzaran los dados para saber cuantas casillas retrocederá")
            input("Preciona una tecla para lanzar los dados...")
            dado1 = rd.randrange(1,6)
            dado2 = rd.randrange(1,6)
            print(f"Resultado de los dados: Dado 1: {dado1} Dado 2: {dado2}")
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
            