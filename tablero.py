import colorama
from colorama import Fore, Back, Style

#tabla con formato
class tablero:
    def mostrarTablero(self, listJugadores,reglas): 
        iconoJugador = ['  ⓵', '  ⓶', '  ⓷', '  ⓸', '  ⓹']
        posicionesJugadores = []
        for k in range(len(listJugadores)):
            posicionesJugadores.append(listJugadores[k].posicionActual)

        tabla = []

        for i in range(1, 101, 10):
            fila = []
            for j in range(i, i+10):
                if j in reglas.casillasPenalizacion:
                    
                    if j in posicionesJugadores:
                        fila.append(Fore.YELLOW + Back.RED +"{:4}".format(iconoJugador[posicionesJugadores.index(j)]) + " " + Back.RESET + Fore.RESET)  
                    else:
                        fila.append(Fore.YELLOW + Back.RED +"{:4}".format(j) + " " + Back.RESET + Fore.RESET)  

                elif j in reglas.casillasSeguras or j in reglas.tunelSeguro:
                    if j in posicionesJugadores:
                        fila.append(Back.CYAN + "{:4}".format(iconoJugador[posicionesJugadores.index(j)]) +" "+ Back.RESET+Fore.RESET)  # Si no es par, imprimir normalmente
                    else:
                        fila.append(Back.CYAN + "{:4}".format(j) +" "+ Back.RESET+Fore.RESET)  # Si no es par, imprimir normalmente

                elif j in reglas.casillasTirosDoble:
                    if j in posicionesJugadores:
                        fila.append(Fore.WHITE + Back.GREEN +"{:4}".format(iconoJugador[posicionesJugadores.index(j)]) +" "+ Back.RESET + Fore.RESET)
                    else:
                        fila.append(Fore.WHITE + Back.GREEN +"{:4}".format(j) +" "+ Back.RESET + Fore.RESET)

                else:
                    if j in posicionesJugadores:
                        fila.append("{:4}".format(iconoJugador[posicionesJugadores.index(j)]) + " ")  
                    elif j == 100:
                        fila.append(Fore.WHITE + Back.LIGHTBLACK_EX +"{:4}".format('  Ⓜ') +" "+ Back.RESET + Fore.RESET)
                    else:
                        fila.append("{:4}".format(j) + " ")  

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


        print('+-----------------------------------------------------------+')
        for fila in tabla:
            
            print('|' + '|'.join(fila)+"|")
            print('+-----------------------------------------------------------+')

        print()