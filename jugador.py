class jugador:
    def __init__(self, id, posicionActual, resultadoDado,cantidadTirosDobles,casillaSeguridad,tunelSeguro):
        self.id = id
        self.posicionActual = posicionActual
        self.resultadoDado = resultadoDado
        self.cantidadTirosDobles = cantidadTirosDobles
        self.casillaSeguridad =casillaSeguridad 
        self.tunelSeguro = tunelSeguro

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
            return True
        else:
            return False
        


import random as rdn
otroJugador = jugador(1,34,[0,0],45,True,True)  

otroJugador.resultadoDado[0] = rdn.randint(1,6)
otroJugador.resultadoDado[1] = rdn.randint(1,6)

print(otroJugador.esPar())