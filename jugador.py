class jugador:
    def __init__(self, id, posicionActual, resultadoDado,tiroDoble,cantidadTirosDobles,casillaSeguridad,tunelSeguro):
        self.id = id #entero para identificar jugador
        self.posicionActual = posicionActual #entero que indica la casilla actual en la que se encuentra el jugador
        self.resultadoDado = resultadoDado #arreglo que contiene los dos valores de los dados lanzados
        self.tiroDoble = tiroDoble #boleano que indica si el jugador va a tirar por segunda vez
        self.cantidadTirosDobles = cantidadTirosDobles #entero que indica la cantidad de veces dobles que ha tirado el jugador
        self.casillaSeguridad =casillaSeguridad #booleano que indica que la casilla en la que se encuentra el jugador es segura
        self.tunelSeguro = tunelSeguro #booleano que indica que el jugador se encuentra en el tunel final del tablero

    #Funcion que sirve para saber si al lanzar los dados cayo en numero par
    def esPar(self):
        par1 = False
        par2 = False

        if self.resultadoDado[0] % 2 == 0:
            print('es par el numero 1')
            par1 = True
        if self.resultadoDado[1] % 2 == 0:
            print('es par el numero 2')
            par2 = True
        
        if par1 and par2:
            self.tiroDoble = True
            self.cantidadTirosDobles += 1 

        else:
            self.tiroDoble = False
        
    #funcion que sirve para mover al jugador
    def cambiarPosicion(self):
            if self.cantidadTirosDobles > 2:
                print(f'El jugador {self.id} a vuelto al inicio porque ha tirado doble tres veces seguida')
                self.cantidadTirosDobles = 0
                self.posicionActual = 1
            elif self.posicionActual<100:
                self.posicionActual += sum(self.resultadoDado) #se suma el valor de ambos dados para que avance
                if self.posicionActual > 100:
                    self.posicionActual = self.posicionActual - 100
        
import random as rdn
otroJugador = jugador(1,34,[0,0],True,45,True,True)  

for i in range(2):
    otroJugador.resultadoDado[i] = rdn.randint(1,6)

otroJugador.esPar()
print("pruba")