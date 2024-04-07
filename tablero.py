import colorama
from colorama import Fore, Back, Style

class Tablero:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas

        #self.celdas = [[f' ⓵ {i+1}' for _ in range(columnas)] for _ in range(filas)]
        self.celdas = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                fila.append(f' Ⓜ {i+1}')
            self.celdas.append(fila)
#⓵ ⓶ ⓷ ⓸ ⓹
    def inicializar_tablero(self):
        # Llena el tablero con celdas vacías
        pass

    def dibujar_tablero(self):
        # Muestra el tablero en la consola
        for fila in self.celdas:
            print('|' + '|'.join(fila) + '|')

# Ejemplo de uso
tablero = Tablero(filas=10, columnas=10)
tablero.inicializar_tablero()
tablero.dibujar_tablero()


# for i in range(1, 101, 10):
#     for j in range(i, i+10):
#         print('{:4}'.format(j), end='')
#     print()

#tabla con formato
tabla = []

for i in range(1, 101, 10):
    fila = []
    for j in range(i, i+10):
        fila.append(j)
    tabla.append(fila)

# Imprimir la lista como tabla con el formato deseado
for fila in tabla:
    for num in fila:
        print("{:4}".format(num), end='')
    print()


tabla1 = []

for i in range(1, 101, 10):
    fila = []
    for j in range(i, i+10):
        fila.append("{:4}".format(j))  # Formateamos los números antes de agregarlos a la fila
    tabla1.append(fila)

# Imprimir la lista como tabla con el formato deseado
for fila1 in tabla1:
    #print('+----+----' * 5 + '+')  # Agregamos la línea horizontal de separación
    print(Back.CYAN + '|' + '|'.join(fila1) + '|' +Back.RESET)
#print('+----+----' * 5 + '+')  # Agregamos la línea horizontal de separación

# print(Fore.RED + 'some red text')
# print(Back.CYAN + 'cyan')
# print(Style.BRIGHT + "BRIGHT")
# print(Fore.RED + Back.GREEN + "red text on green back" + Back.RESET)
# from colorama import Back, init

# init(autoreset=True)  # Inicializar colorama y configurarlo para restablecer automáticamente el color después de cada impresión

tabla = []
posicionPrueba = '  ⓹'
for i in range(1, 101, 10):
    fila = []
    for j in range(i, i+10):
        if j in [13,88,87,15,82,22,77,44,39,24]:  # Verificar si el número es par
            if j == 88:
                fila.append(Fore.YELLOW + Back.RED +"{:4}".format(posicionPrueba) + " " + Back.RESET + Fore.RESET)  # Si es par, imprimir en amarillo
            else:
                fila.append(Fore.YELLOW + Back.RED +"{:4}".format(j) + " " + Back.RESET + Fore.RESET)  # Si es par, imprimir en amarillo

        elif j in [57,46,4,49,91,18,8,55,85,60] or j in [95,96,97,98,99]:
            fila.append(Back.CYAN + "{:4}".format(j) +" "+ Back.RESET+Fore.RESET)  # Si no es par, imprimir normalmente
        elif j in [36,73,2,56,16]:
            fila.append(Fore.WHITE + Back.GREEN +"{:4}".format(j) +" "+ Back.RESET + Fore.RESET)
        else:
            fila.append("{:4}".format(j) + " ")  # Si no es par, imprimir normalmente
    tabla.append(fila)

# Imprimir la lista como tabla con el formato deseado
print("INICIO")
for fila in tabla:
    print('|' + '|'.join(fila)+"|")

