import os
import subprocess
#Libreria que debe ser descargada con pip colorama, sirve para mostrar colores en consola.
import colorama
from colorama import Fore, Back, Style
#Fore es el color del texto mostrado en pantalla
#Back es el color de fondo del texto mostrado en pantalla
#Style es el tipo de letra que se muestra como negrita por ejemplo

#Variable que contiene el titulo del juego, en un tipo de letra especifico.
titulo = f'''
{Fore.CYAN}░█─── █▀▀█ █▀▀ 　 ░█▀▀█ █▀▀█ █▀▀ ─▀─ █── █── █▀▀█ █▀▀{Fore.RESET} 　 {Fore.RED}░█▀▄▀█ ─█▀▀█ ░█─── ░█▀▀▄ ▀█▀ ▀▀█▀▀ ─█▀▀█ ░█▀▀▀█{Fore.RESET} 
{Fore.CYAN}░█─── █▄▄█ ▀▀█ 　 ░█─── █▄▄█ ▀▀█ ▀█▀ █── █── █▄▄█ ▀▀█{Fore.RESET} 　 {Fore.RED}░█░█░█ ░█▄▄█ ░█─── ░█─░█ ░█─ ─░█── ░█▄▄█ ─▀▀▀▄▄{Fore.RESET} 
{Fore.CYAN}░█▄▄█ ▀──▀ ▀▀▀ 　 ░█▄▄█ ▀──▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀──▀ ▀▀▀{Fore.RESET} 　 {Fore.RED}░█──░█ ░█─░█ ░█▄▄█ ░█▄▄▀ ▄█▄ ─░█── ░█─░█ ░█▄▄▄█{Fore.RESET}'''

#Variable que contiene la frase bienvenido al juego, en un tipo de letra especifico.
bienvenida=f'''
{Fore.CYAN}░█▀▀█ ─▀─ █▀▀ █▀▀▄ ▀█─█▀ █▀▀ █▀▀▄ ─▀─ █▀▀▄ █▀▀█{Fore.RESET} 　 {Fore.RED}█▀▀█ █── 　 ──▀ █──█ █▀▀ █▀▀▀ █▀▀█{Fore.RESET} 
{Fore.CYAN}░█▀▀▄ ▀█▀ █▀▀ █──█ ─█▄█─ █▀▀ █──█ ▀█▀ █──█ █──█{Fore.RESET} 　 {Fore.RED}█▄▄█ █── 　 ──█ █──█ █▀▀ █─▀█ █──█{Fore.RESET} 
{Fore.CYAN}░█▄▄█ ▀▀▀ ▀▀▀ ▀──▀ ──▀── ▀▀▀ ▀──▀ ▀▀▀ ▀▀▀─ ▀▀▀▀{Fore.RESET} 　 {Fore.RED}▀──▀ ▀▀▀ 　 █▄█ ─▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀▀{Fore.RESET}\n'''

#Funcion que sirve para limpiar la consola
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#Variable que contiene el texto con cada una de las instrucciones del juego
instrucciones=f'''\n{Style.BRIGHT}Bienvenido al juego de “Las casillas malditas”{Style.RESET_ALL}
El juego consiste en que cada jugador debe lanzar los dados para saber cuantas casillas debe avanzar, 
cada jugador comenzara en la casilla de inicio, también conocida como cero, para salir de ahí debes 
obtener par en los dados, para luego moverte a la casilla correspondiente.

Si sacas par en los dados, sales de inicio y te posicionas en la casilla que resulte de la suma de 
ambos dados, si sacas par estando fuera de inicio, volverás a tirar, si sacas tres veces seguidas par,
volverás a inicio.

En este juego hay {Back.CYAN} casillas seguras {Back.RESET} ,{Back.GREEN} casillas de tiro doble {Back.RESET} y como no,{Back.RED} LAS CASILLAS MALDITAS.{Back.RESET}

Una casilla segura es aquella donde no podrán comer tu ficha (Aparecen en el tablero con color {Fore.CYAN}CYAN{Fore.RESET})
si un jugador alcanza tu misma casilla, si tu ficha es comida, retrocedes 3 casillas y el jugador que 
comió avanza 10 casillas.

Tambien existe un tunel seguro, el cual son las ultimas 5 casillas antes de la meta, en este tunel
NADIE podra ser comido (Aparecen en el tablero con color {Fore.CYAN}CYAN{Fore.RESET}).

Las casillas de tiro doble (Aparecen en el tablero con color {Fore.GREEN}VERDE{Fore.RESET}) te permiten volver a realizar 
otra vez, si en dado caso habías sacado par antes de caer en esta casilla, y sacas pares al realizar 
el tiro, este no se sumará a los tiros dobles que se llevaba, ya que es una bonificación del juego, 
pero, si sacas par en tu secundo tiro de casilla doble, este si se contabilizara.

Las casillas malditas (Aparecen en el tablero con color {Fore.RED}ROJO{Fore.RESET}) consisten en que, si caes en una de 
estas casillas, deberás lanzar los dados, y el número que resulte, será la cantidad de casillas que 
deberás retroceder, si vuelves a caer en una casilla maldita, volverás a tirar los dados y volver a 
retroceder, si caes encima de otro jugador al haber llegado de una casilla maldita, este jugador 
retrocede 3 casillas, pero tu no podrás avanzar las 10 adicionales, si no que deberás quedarte en 
esa casilla.\n'''

#Funcion que sirve para mostrar el menu principal
def menu():
    clear_console()
    print(titulo)
    
    #Se verifica si el usuario ingreso un valor numero, al intertar convertirlo si da error el try, se sale del juego
    try:
        op = int(input('\n1-Instrucciones.\n2-Comenzar partida.\n3-Presione enter o ingrese cualquier caracter para salir.\n'))
    except:
        print('¡Haz salido del juego!')
        exit()

    #Se verifica si el jugador desea ver las instrucciones del juego (Op es la opcion que ingreso el usuario)
    if(op == 1):
        #Se limpia consola
        clear_console()
        
        print(titulo)
        print(instrucciones)
        input('Presione cualquier tecla para volver al menu principal.\n')
        #Se vuelve a llamar la funcion para que menu() para que el usuario seleccione una opcion o salga del juego
        menu()
    #Se verfica si el jugador a ingresado que desea comenzar la partida
    elif(op == 2):
        clear_console()
        print(bienvenida)

        #Aqui se está ejecutando el script main.py desde el script actual, utilizando el intérprete de Python.
        #Que es el que contiene todas las funciones del juego
        subprocess.run(['python', 'main.py'])
        #Una vez termina el juego.
        #Se vuelve a llamar la funcion para que menu() para que el usuario seleccione una opcion o salga del juego
        menu()
#Se llama la funcion menu para que realice sus procesos
menu()