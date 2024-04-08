import colorama
from colorama import Fore, Back, Style

#tabla con formato
class tablero:
    def mostrarTablero(self, listJugadores): 
        iconoJugador = ['  ⓵', '  ⓶', '  ⓷', '  ⓸', '  ⓹']
        posicionesJugadores = []
        for k in range(len(listJugadores)):
            posicionesJugadores.append(listJugadores[k].posicionActual)

        tabla = []

        for i in range(1, 101, 10):
            fila = []
            for j in range(i, i+10):
                if j in [13,88,87,15,82,22,77,44,39,24]:  # Verificar si el número es par
                    
                    if j in posicionesJugadores:
                        fila.append(Fore.YELLOW + Back.RED +"{:4}".format(iconoJugador[posicionesJugadores.index(j)]) + " " + Back.RESET + Fore.RESET)  # Si es par, imprimir en amarillo
                    else:
                        fila.append(Fore.YELLOW + Back.RED +"{:4}".format(j) + " " + Back.RESET + Fore.RESET)  # Si es par, imprimir en amarillo

                elif j in [57,46,4,49,91,18,8,55,85,60] or j in [95,96,97,98,99]:
                    if j in posicionesJugadores:
                        fila.append(Back.CYAN + "{:4}".format(iconoJugador[posicionesJugadores.index(j)]) +" "+ Back.RESET+Fore.RESET)  # Si no es par, imprimir normalmente
                    else:
                        fila.append(Back.CYAN + "{:4}".format(j) +" "+ Back.RESET+Fore.RESET)  # Si no es par, imprimir normalmente

                elif j in [36,73,2,56,16]:
                    if j in posicionesJugadores:
                        fila.append(Fore.WHITE + Back.GREEN +"{:4}".format(iconoJugador[posicionesJugadores.index(j)]) +" "+ Back.RESET + Fore.RESET)
                    else:
                        fila.append(Fore.WHITE + Back.GREEN +"{:4}".format(j) +" "+ Back.RESET + Fore.RESET)

                else:
                    if j in posicionesJugadores:
                        fila.append("{:4}".format(iconoJugador[posicionesJugadores.index(j)]) + " ")  # Si no es par, imprimir normalmente
                    else:
                        fila.append("{:4}".format(j) + " ")  # Si no es par, imprimir normalmente

            tabla.append(fila)

        # Imprimir la lista como tabla con el formato deseado
        print('+-----------------------------+')
        print('|            INICIO           |')
        print('|', end='')
        # Asegúrate de que el número ingresado por el usuario no supere la longitud del arreglo iconoJugador
        #jugadores = min(jugadores, len(iconoJugador))

        # Itera sobre los jugadores e imprime los iconos correspondientes
        for i in range(len(listJugadores)):
            if listJugadores[i].posicionActual > 0:
                continue
            else: 
                print(iconoJugador[i], end=' ')
            
        print('\n+-----------------------------+\n')


        for fila in tabla:
            print('|' + '|'.join(fila)+"|")
        print()