#Libreria para generar numeros random
import random as rdn
#Se importa la clase juego, que contiene las casillas y las mecanicas del juego.
from juego import juego
#Libreria que debe ser descargada con pip colorama, sirve para mostrar colores en consola.
import colorama
from colorama import Fore, Back, Style
#Fore es el color del texto mostrado en pantalla
#Back es el color de fondo del texto mostrado en pantalla
#Style es el tipo de letra que se muestra como negrita por ejemplo

class jugador:
    def __init__(self, id, posicionActual, resultadoDado,tiroDoble,cantidadTirosDobles,penalizacion,salidaInicio):
        self.id = id #entero para identificar jugador
        self.posicionActual = posicionActual #entero que indica la casilla actual en la que se encuentra el jugador
        self.resultadoDado = resultadoDado #arreglo que contiene los dos valores de los dados lanzados
        self.tiroDoble = tiroDoble #boleano que indica si el jugador va a tirar por segunda vez
        self.cantidadTirosDobles = cantidadTirosDobles #entero que indica la cantidad de veces dobles que ha tirado el jugador
        self.penalizacion = penalizacion #boooleano que indica si un jugador fue penalizado
        self.salidaInicio = salidaInicio #booleano que indica si el jugado ha sacado par y este se encuentra en partida

    #Funcion que sirve para saber si al lanzar los dados cayo en numero par
    def esPar(self, Boolpartida):
        # Verifica si el resultado de los dados es un par
        if self.resultadoDado[0] == self.resultadoDado[1]:
            # Si el resultado es un par
            if Boolpartida:
                # Si la partida está en curso
                self.tiroDoble = True
                self.cantidadTirosDobles += 1
                # Si el jugador ha obtenido dobles menos de dos veces seguidas
                if(self.cantidadTirosDobles <= 2):
                    # Imprime un mensaje indicando que el jugador ha obtenido dobles y puede volver a tirar
                    print(f"{Back.GREEN}Haz obtenido dobles!!!!{Back.RESET}\nPuedes volver a tirar.")
            else:
                # Si la partida no está en curso, el jugador sale de inicio
                self.salidaInicio = True
                print(Fore.GREEN + f"Jugador {self.id} ha salido de inicio porque haz sacado par" + Fore.RESET)
        else:
            # Si el resultado no es un par
            if not Boolpartida:
                # Si la partida no está en curso, imprime un mensaje indicando que el jugador no puede salir de inicio
                print(Fore.RED + f"No haz sacado par, por lo tanto no saldras de inicio." + Fore.RESET)
            self.tiroDoble = False
            self.cantidadTirosDobles = 0

        
        
    #Funcion que sirve para mover al jugador
    def cambiarPosicion(self):
        # Verifica si la posición actual del jugador es menor que 100
        if self.posicionActual < 100:
            # Suma el valor de ambos dados para avanzar
            self.posicionActual += sum(self.resultadoDado)
            # Verifica si el jugador ha pasado la casilla 100
            if self.posicionActual > 100:
                # Calcula cuánto se pasó de la casilla 100
                extra = self.posicionActual - 100
                # Establece la posición actual como 100, retrocediendo la cantidad extra
                self.posicionActual = self.posicionActual - extra
            # Imprime un mensaje indicando la nueva posición del jugador
            print(f"{Style.BRIGHT} Te mueves a la casilla: {self.posicionActual}{Style.RESET_ALL}")
            # Verifica si la nueva posición del jugador es una casilla segura
            if self.posicionActual in juego.casillasSeguras:
                # Imprime un mensaje indicando que el jugador ha caído en una casilla segura
                print(f'{Back.BLUE}Felicidades haz caido en una casilla segura!!!{Back.RESET}\nSignifica que no podran comerte si otro jugador cae en esta casilla.')
            # Verifica si la nueva posición del jugador es un túnel seguro
            elif self.posicionActual in juego.tunelSeguro:
                # Imprime un mensaje indicando que el jugador ha llegado a un túnel seguro
                print(f'{Back.BLUE}Felicidades haz llegado al tunel seguro!!!{Back.RESET}\nApartir de ahora NADIE podra comerte.')

    #Funcion que sirve para lanzar los dados en cada turno de cada jugador
    def lanzamientoInicial(self):
        # Imprime un mensaje indicando que se están lanzando los dados
        print("\nLanzando dados...")
        # Genera números aleatorios para representar los resultados de los dados
        self.resultadoDado[0] = rdn.randrange(1, 6)
        self.resultadoDado[1] = rdn.randrange(1, 6)
        # Imprime el resultado de los dados
        print(f"{Style.BRIGHT}Resultado de los dados: {self.resultadoDado[0]} y {self.resultadoDado[1]}{Style.RESET_ALL}")
        # Llama a la función 'esPar' para verificar si se ha obtenido un par en el lanzamiento inicial
        self.esPar(self.salidaInicio)

    #Funcion que se llama cuando el juagdor cae en una casilla de tiro doble
    def lanzamientoDeBonificacion(self):
        # Imprime un mensaje indicando que se están lanzando los dados
        print("\nLanzando dados...")
        # Genera números aleatorios para representar los resultados de los dados
        self.resultadoDado[0] = rdn.randrange(1, 6)
        self.resultadoDado[1] = rdn.randrange(1, 6)
        # Imprime el resultado de los dados
        print(f"{Style.BRIGHT}Resultado de los dados: {self.resultadoDado[0]} y {self.resultadoDado[1]}{Style.RESET_ALL}")
        # Realiza el cambio de posición del jugador según el resultado de los dados
        self.cambiarPosicion()
        # Verifica si el jugador obtuvo dobles antes de caer en la casilla
        if self.tiroDoble:
            # Imprime un mensaje indicando que el jugador volverá a tirar porque había obtenido dobles antes de caer en la casilla
            print(f"{Fore.GREEN}Volveras a tirar ya que habias dobles antes de caer en la casilla{Fore.RESET}")
    