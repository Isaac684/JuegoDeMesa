#Libreria que debe ser descargada con pip colorama, sirve para mostrar colores en consola.
import colorama
from colorama import Fore, Back, Style
#Fore es el color del texto mostrado en pantalla
#Back es el color de fondo del texto mostrado en pantalla
#Style es el tipo de letra que se muestra como negrita por ejemplo

#Clase tablero que contiene todas las casillas del tablero con los jugadores en partida
class tablero:
    #Funcion que sirve para mostrar el tablero en consola
    #Recibe como parametros una lista con objetos de la clase 'jugador' asi como las reglas del juego
    #que es un objeto de la clase 'juego'
    def mostrarTablero(self, listJugadores,reglas): 
        #Variable que contiene los iconos 1,2,3,4,5 que representa a cada jugador correspondiente
        iconoJugador = ['  ⓵', '  ⓶', '  ⓷', '  ⓸', '  ⓹']
        #Arreglo que contiene la posicion de cada jugador
        posicionesJugadores = []

        #Bocle for con el que se itera la lista de jugadores y se agrega la posicion de cada jugador al arreglo posicionesJugadores
        for k in range(len(listJugadores)):
            posicionesJugadores.append(listJugadores[k].posicionActual)

        # Creamos una lista vacía para almacenar las filas de la tabla
        tabla = []

        # Iteramos sobre un rango de números del 1 al 101 (excluyendo el 101) de 10 en 10
        for i in range(1, 101, 10):
            # Creamos una lista vacía para almacenar los elementos de una fila
            fila = []
            # Iteramos sobre un rango de números desde 'i' hasta 'i+10' (excluyendo 'i+10')
            for j in range(i, i+10):
                # Verificamos si 'j' está en las casillas de penalización definidas en 'reglas.casillasPenalizacion'
                if j in reglas.casillasPenalizacion:
                    # Si 'j' está en las posiciones de los jugadores, agregamos el icono del jugador en amarillo sobre fondo rojo
                    # de lo contrario, agregamos el número en amarillo sobre fondo rojo
                    if j in posicionesJugadores:
                        fila.append(Fore.YELLOW + Back.RED + "{:4}".format(iconoJugador[posicionesJugadores.index(j)]) + " " + Back.RESET + Fore.RESET)  
                    else:
                        fila.append(Fore.YELLOW + Back.RED + "{:4}".format(j) + " " + Back.RESET + Fore.RESET)  

                # Verificamos si 'j' está en las casillas seguras o en el túnel seguro definidos en 'reglas.casillasSeguras' y 'reglas.tunelSeguro'
                elif j in reglas.casillasSeguras or j in reglas.tunelSeguro:
                    # Si 'j' está en las posiciones de los jugadores, agregamos el icono del jugador sobre fondo cyan
                    # de lo contrario, agregamos el número sobre fondo cyan
                    if j in posicionesJugadores:
                        fila.append(Back.CYAN + "{:4}".format(iconoJugador[posicionesJugadores.index(j)]) + " " + Back.RESET + Fore.RESET) 
                    else:
                        fila.append(Back.CYAN + "{:4}".format(j) + " " + Back.RESET + Fore.RESET)

                # Verificamos si 'j' está en las casillas de tiros dobles definidos en 'reglas.casillasTirosDoble'
                elif j in reglas.casillasTirosDoble:
                    # Si 'j' está en las posiciones de los jugadores, agregamos el icono del jugador en blanco sobre fondo verde
                    # de lo contrario, agregamos el número en blanco sobre fondo verde
                    if j in posicionesJugadores:
                        fila.append(Fore.WHITE + Back.GREEN + "{:4}".format(iconoJugador[posicionesJugadores.index(j)]) + " " + Back.RESET + Fore.RESET)
                    else:
                        fila.append(Fore.WHITE + Back.GREEN + "{:4}".format(j) + " " + Back.RESET + Fore.RESET)

                # Si 'j' no cumple ninguna de las condiciones anteriores
                else:
                    # Si 'j' está en las posiciones de los jugadores, agregamos el icono del jugador
                    # Si 'j' es igual a 100, agregamos el símbolo 'Ⓜ' en blanco sobre fondo negro claro
                    # de lo contrario, agregamos el número
                    if j in posicionesJugadores:
                        fila.append("{:4}".format(iconoJugador[posicionesJugadores.index(j)]) + " ")  
                    elif j == 100:
                        fila.append(Fore.WHITE + Back.LIGHTBLACK_EX + "{:4}".format(' Ⓜ') + " " + Back.RESET + Fore.RESET)
                    else:
                        fila.append("{:4}".format(j) + " ")  

            # Agregamos la fila a la tabla
            tabla.append(fila)


        # Imprimir la lista como tabla con el formato deseado
        print('+-----------------------------+')
        print('|            INICIO           |')
        print('|', end='')

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