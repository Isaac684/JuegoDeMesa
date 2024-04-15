import random as rdn
from juego import juego
import colorama
from colorama import Fore, Back, Style
class jugador:
    def __init__(self, id, posicionActual, resultadoDado,tiroDoble,cantidadTirosDobles,penalizacion,salidaInicio):
        self.id = id #entero para identificar jugador
        self.posicionActual = posicionActual #entero que indica la casilla actual en la que se encuentra el jugador
        self.resultadoDado = resultadoDado #arreglo que contiene los dos valores de los dados lanzados
        self.tiroDoble = tiroDoble #boleano que indica si el jugador va a tirar por segunda vez
        self.cantidadTirosDobles = cantidadTirosDobles #entero que indica la cantidad de veces dobles que ha tirado el jugador
        self.penalizacion = penalizacion #boooleano que indica si un jugador fue penalizado
        self.salidaInicio = salidaInicio #booleano que indica si el jugado ha sacado par y este sale de inicio

    #Funcion que sirve para saber si al lanzar los dados cayo en numero par
    def esPar(self,Boolpartida):
        if self.resultadoDado[0] == self.resultadoDado[1]:
            if Boolpartida: 
                self.tiroDoble = True
                self.cantidadTirosDobles += 1
                if(self.cantidadTirosDobles<=2):    
                    print(f"{Back.GREEN}Haz obtenido dobles!!!!{Back.RESET}\nPuedes volver a tirar.")
            else:
                self.salidaInicio = True
                print(Fore.GREEN + f"Jugador {self.id} ha salido de la meta porque haz sacado par"+Fore.RESET)
        elif not Boolpartida:
            
            print(Fore.RED+f"No haz sacado par, por lo tanto no saldras de la meta."+Fore.RESET)

        else:
            self.tiroDoble = False
            self.cantidadTirosDobles = 0
        
        
    #funcion que sirve para mover al jugador
    def cambiarPosicion(self):
            if self.posicionActual<100:
                self.posicionActual += sum(self.resultadoDado) #se suma el valor de ambos dados para que avance
                if self.posicionActual > 100:
                    extra = self.posicionActual - 100
                    self.posicionActual = self.posicionActual - extra
                print(f"{Style.BRIGHT} Te mueves a la casilla: {self.posicionActual}{Style.RESET_ALL}")
                if self.posicionActual in juego.casillasSeguras:
                    print(f'{Back.BLUE}Felicidades haz caido en una casilla segura!!!{Back.RESET}\nSignifica que no podran comerte si otro jugador cae en esta casilla.')
                elif self.posicionActual in juego.tunelSeguro:
                    print(f'{Back.BLUE}Felicidades haz llegado al tunel seguro!!!{Back.RESET}\nApartir de ahora NADIE podra comerte.')

    def lanzamientoInicial(self):
        print("\nLanzando dados...")
        self.resultadoDado[0] = rdn.randrange(1,6)
        self.resultadoDado[1] = rdn.randrange(1,6)
        print(f"{Style.BRIGHT}Resultado de los dados: {self.resultadoDado[0]} y {self.resultadoDado[1]}{Style.RESET_ALL}")
        self.esPar(self.salidaInicio)

    def lanzamientoDeBonificacion(self):
        print("\nLanzando dados...")
        self.resultadoDado[0] = rdn.randrange(1,6)
        self.resultadoDado[1] = rdn.randrange(1,6)
        print(f"{Style.BRIGHT}Resultado de los dados: {self.resultadoDado[0]} y {self.resultadoDado[1]}{Style.RESET_ALL}")
        self.cambiarPosicion()
        if self.tiroDoble:
            print(f"{Fore.GREEN}Volveras a tirar ya que habias dobles antes de caer en la casilla{Fore.RESET}")