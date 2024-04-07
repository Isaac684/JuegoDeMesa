import random as rdn
from juego import juego

class jugador:
    def __init__(self, id, posicionActual, resultadoDado,tiroDoble,cantidadTirosDobles,penalizacion,salidaMeta):
        self.id = id #entero para identificar jugador
        self.posicionActual = posicionActual #entero que indica la casilla actual en la que se encuentra el jugador
        self.resultadoDado = resultadoDado #arreglo que contiene los dos valores de los dados lanzados
        self.tiroDoble = tiroDoble #boleano que indica si el jugador va a tirar por segunda vez
        self.cantidadTirosDobles = cantidadTirosDobles #entero que indica la cantidad de veces dobles que ha tirado el jugador
        self.penalizacion = penalizacion #boooleano que indica si un jugador fue penalizado
        self.salidaMeta = salidaMeta #booleano que indica si el jugado ha sacado par y este sale a partida

    #Funcion que sirve para saber si al lanzar los dados cayo en numero par
    def esPar(self,Boolpartida):
        if self.resultadoDado[0] == self.resultadoDado[1]:
            if Boolpartida: 
                print("Haz obtenido dobles!!!!\nPuedes volver a tirar.")
                self.tiroDoble = True
                self.cantidadTirosDobles += 1
            else:
                self.salidaMeta = True
                print(f"Jugador {self.id} ha salido de la meta porque haz sacado par")
        elif not Boolpartida:
            
            print(f"No haz sacado par, por lo tanto no saldras de la meta.")

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
                print(f"Te mueves a la casilla: {self.posicionActual}")
                if self.posicionActual in juego.casillasSeguras:
                    print('Felicidades haz caido en una casilla segura!!!\nSignifica que no podran comerte si otro jugador cae en esta casilla :)')
                elif self.posicionActual in juego.tunelSeguro:
                    print('Felicidades haz llegado al tunel seguro!!!\nApartir de ahora NADIE podra comerte.')

    def lanzamientoInicial(self):
        print("\nLanzando dados...")
        self.resultadoDado[0] = rdn.randrange(1,6)
        self.resultadoDado[1] = rdn.randrange(1,6)
        print(f"Dado 1: {self.resultadoDado[0]} Dado 2: {self.resultadoDado[1]}")
        self.esPar(self.salidaMeta)

    def lanzamientoDeBonificacion(self):
        print("\nLanzando dados...")
        self.resultadoDado[0] = rdn.randrange(1,6)
        self.resultadoDado[1] = rdn.randrange(1,6)
        print(f"Dado 1: {self.resultadoDado[0]} Dado 2: {self.resultadoDado[1]}")
        self.cambiarPosicion()
        if self.tiroDoble:
            print("Volveras a tirar ya que habias dobles antes de caer en la casilla")