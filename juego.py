class juego:
    casillasSeguras = [57,46,4,49,91,18,8,55,85,60]
    casillasPenalizacion = [9,88,87,15,82,22,77,44,39,24]
    casillasTirosDoble = [36,73,2,56,7]
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

        return listJugadores
