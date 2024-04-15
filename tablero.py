import colorama
from colorama import Fore, Back, Style  # Importa los estilos de color de la librería Colorama

# Define la clase Tablero
class tablero:
    # Método para mostrar el tablero con formato
    def mostrarTablero(self, listJugadores, reglas): 
        iconoJugador = ['  ⓵', '  ⓶', '  ⓷', '  ⓸', '  ⓹']  # Iconos para representar a los jugadores en el tablero
        posicionesJugadores = []  # Lista para almacenar las posiciones actuales de los jugadores

        # Obtiene las posiciones actuales de los jugadores
        for k in range(len(listJugadores)):
            posicionesJugadores.append(listJugadores[k].posicionActual)

        tabla = []  # Lista para almacenar las filas del tablero

        # Construye la tabla del tablero
        for i in range(1, 101, 10):
            fila = []  # Lista para almacenar una fila del tablero
            for j in range(i, i+10):
                # Verifica en qué tipo de casilla se encuentra y asigna el formato correspondiente
                if j in reglas.casillasPenalizacion:
                    if j in posicionesJugadores:
                        fila.append(Fore.YELLOW + Back.RED + "{:4}".format(iconoJugador[posicionesJugadores.index(j)]) + " " + Back.RESET + Fore.RESET)  
                    else:
                        fila.append(Fore.YELLOW + Back.RED + "{:4}".format(j) + " " + Back.RESET + Fore.RESET)  

                elif j in reglas.casillasSeguras or j in reglas.tunelSeguro:
                    if j in posicionesJugadores:
                        fila.append(Back.CYAN + "{:4}".format(iconoJugador[posicionesJugadores.index(j)]) + " " + Back.RESET + Fore.RESET)
                    else:
                        fila.append(Back.CYAN + "{:4}".format(j) + " " + Back.RESET + Fore.RESET)

                elif j in reglas.casillasTirosDoble:
                    if j in posicionesJugadores:
                        fila.append(Fore.WHITE + Back.GREEN + "{:4}".format(iconoJugador[posicionesJugadores.index(j)]) + " " + Back.RESET + Fore.RESET)
                    else:
                        fila.append(Fore.WHITE + Back.GREEN + "{:4}".format(j) + " " + Back.RESET + Fore.RESET)

                else:
                    if j in posicionesJugadores:
                        fila.append("{:4}".format(iconoJugador[posicionesJugadores.index(j)]) + " ")  
                    elif j == 100:
                        fila.append(Fore.WHITE + Back.LIGHTBLACK_EX + "{:4}".format('  Ⓜ') + " " + Back.RESET + Fore.RESET)
                    else:
                        fila.append("{:4}".format(j) + " ")  

            tabla.append(fila)  # Agrega la fila a la tabla

        # Imprime el encabezado del tablero
        print('+-----------------------------+')
        print('|            INICIO           |')
        print('|', end='')

        # Itera sobre los jugadores e imprime los iconos correspondientes en el inicio
        for i in range(len(listJugadores)):
            if listJugadores[i].posicionActual > 0:
                continue
            else: 
                print(iconoJugador[i], end=' ')
            
        print('\n+-----------------------------+\n')

        # Imprime el cuerpo del tablero
        print('+-----------------------------------------------------------+')
        for fila in tabla:
            print('|' + '|'.join(fila) + "|")
            print('+-----------------------------------------------------------+')

        print()  # Imprime una línea en blanco al final
