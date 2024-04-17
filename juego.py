# Importación del módulo 'random' como 'rd' para generación de números aleatorios
import random as rd

# Importación de la clase Tablero desde el archivo 'tablero.py'
from tablero import tablero

# Importación de la librería 'colorama' para añadir color a la salida en la consola
import colorama
from colorama import Fore, Back, Style

# Creación de una instancia de la clase Tablero
tabla = tablero()

# Definición de la clase Juego
class juego:
    # Definición de listas de casillas especiales y valores de juego
    casillasSeguras = [4, 8, 18, 46, 49, 55, 57, 60, 85, 91]
    casillasPenalizacion = [13, 15, 22, 24, 39, 44, 77, 82, 88, 94]
    casillasTirosDoble = [2, 16, 36, 56, 73]
    tunelSeguro = [95, 96, 97, 98, 99]
    meta = 100
    juegoFinalizado = False

    # Método para aplicar la mecánica de 'comer' a otros jugadores
    def mecanicaComer(self, posicionJugadorActual, listJugadores):
        for i in range(len(listJugadores)):
            if posicionJugadorActual == i:
                continue
            else:
                if listJugadores[posicionJugadorActual].posicionActual == listJugadores[i].posicionActual:
                    if listJugadores[i].posicionActual in self.casillasSeguras:
                        # Si el jugador está en una casilla segura
                        print(f"{Back.YELLOW}El jugador {listJugadores[i].id} se ha salvado de ser comido ya que se encuentra en una casilla segura{Back.RESET}")
                        tabla.mostrarTablero(listJugadores,self)     
                    elif listJugadores[i].posicionActual in self.tunelSeguro:
                        # Si el jugador está en un túnel seguro
                        print(f"{Back.YELLOW}El jugador {listJugadores[i].id} se ha salvado de ser comido ya que se encuentra en el túnel seguro{Back.RESET}")
                        tabla.mostrarTablero(listJugadores,self)     
                    else:
                        # Si el jugador es 'comido' por otro
                        print(f"{Back.MAGENTA}El jugador {listJugadores[posicionJugadorActual].id} ha comido al jugador {listJugadores[i].id}{Back.RESET}")
                        print(f"{Fore.RED}Por lo que el jugador {listJugadores[i].id} retrocede 3 casillas!{Fore.RESET}")
                        # Retroceso del jugador 'comido' y posible avance del jugador actual
                        listJugadores[i].posicionActual -= 3
                        if listJugadores[i].posicionActual <= 0:
                            listJugadores[i].posicionActual = 1
                            # Manejo especial si el jugador 'comido' está en la casilla 0
                            print(f"{Style.BRIGHT}Se mueve a la casilla: {listJugadores[i].posicionActual}{Style.RESET_ALL}")
                            if listJugadores[posicionJugadorActual].penalizacion == False:
                                print(f"{Fore.GREEN}Y el jugador {listJugadores[posicionJugadorActual].id} avanzará 10 casillas!!{Fore.RESET}")
                                listJugadores[posicionJugadorActual].posicionActual += 10
                                print(f"{Style.BRIGHT}Te mueves a la casilla: {listJugadores[posicionJugadorActual].posicionActual}{Style.RESET_ALL}")
                                self.casillaPenalizacion(posicionJugadorActual,listJugadores)
                                tabla.mostrarTablero(listJugadores,self)                   
                            else: 
                                # Si el jugador actual tiene penalización
                                print(f'{Back.YELLOW}Debido a que vienes de una casilla de penalización, no podrás avanzar las 10 casillas adicionales por haber comido al jugador {listJugadores[i].id}{Back.RESET}')
                                tabla.mostrarTablero(listJugadores,self)     
                        else:
                            # Retroceso del jugador 'comido'
                            print(f"Se mueve a la casilla: {listJugadores[i].posicionActual}")
                            if listJugadores[posicionJugadorActual].penalizacion == False:
                                print(f"{Fore.GREEN}Y el jugador {listJugadores[posicionJugadorActual].id} avanzará 10 casillas!!{Fore.RESET}")
                                listJugadores[posicionJugadorActual].posicionActual += 10
                                print(f"{Style.BRIGHT}Te mueves a la casilla: {listJugadores[posicionJugadorActual].posicionActual}{Style.RESET_ALL}")
                                self.casillaPenalizacion(posicionJugadorActual,listJugadores)
                                tabla.mostrarTablero(listJugadores,self)     
                            else: 
                                # Si el jugador actual tiene penalización
                                print(f'{Back.YELLOW}Debido a que vienes de una casilla de penalización, no podrás avanzar las 10 casillas adicionales por haber comido al jugador {listJugadores[i].id}{Back.RESET}')
                                tabla.mostrarTablero(listJugadores,self)     
        return listJugadores

    # Método para aplicar la penalización por caer en una casilla de penalización
    def casillaPenalizacion(self, posicionActual,listJugadores):
        if listJugadores[posicionActual].posicionActual in self.casillasPenalizacion:
            # Si el jugador cae en una casilla de penalización
            listJugadores[posicionActual].penalizacion = True
            print(f"\n{Back.RED}El jugador {listJugadores[posicionActual].id} ha caído en una casilla de penalización!{Back.RESET}")
            print(f"Por lo cual se lanzarán los dados para saber cuántas casillas retrocederá")
            input("Presiona una tecla para lanzar los dados...")
            # Generación de dos números aleatorios simulando el lanzamiento de dados
            dado1 = rd.randrange(1,6)
            dado2 = rd.randrange(1,6)
            print(f"\nResultado de los dados: {dado1} Y {dado2}")
            print(f"{Fore.RED}Por lo que el jugador {listJugadores[posicionActual].id} deberá retroceder {(dado1+dado2)} casillas{Fore.RESET}")
            # Aplicación del retroceso
            listJugadores[posicionActual].posicionActual -= (dado1+dado2)
            listJugadores[posicionActual].tiroDoble = False
            print(f"{Style.BRIGHT}Te mueves a la casilla: {listJugadores[posicionActual].posicionActual}{Style.RESET_ALL}")
            tabla.mostrarTablero(listJugadores,self)             
            self.casillaPenalizacion(posicionActual,listJugadores)
            # Llamada recursiva para manejar posibles nuevas casillas de penalización
            self.mecanicaComer(posicionActual,listJugadores)
        return listJugadores

    # Método para manejar la bonificación por caer en una casilla de tiro doble
    def casillaTiroDoble(self, posicionJugadorActual, listJugadores):
        if listJugadores[posicionJugadorActual].posicionActual in self.casillasTirosDoble:
            # Si el jugador cae en una casilla de bonificación de tiro doble
            print(f'El jugador {listJugadores[posicionJugadorActual].id} ha caído en una casilla de bonificación de tiro doble, por lo tanto volverá a tirar')       
            input()
            listJugadores[posicionJugadorActual].lanzamientoDeBonificacion()
            tabla.mostrarTablero(listJugadores,self)     
            self.casillaPenalizacion(posicionJugadorActual,listJugadores)
            self.mecanicaComer(posicionJugadorActual,listJugadores)
            # Se devuelve la lista de jugadores actualizada
            return listJugadores
        else:
            return listJugadores