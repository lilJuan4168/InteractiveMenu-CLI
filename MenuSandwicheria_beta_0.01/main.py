from time import sleep
from os import system
#from progress.bar import ChargingBar
from objetos import *
from funciones import *
from comidas import *

menu = Menu(comidas_list)
menu.listar_menu()
usuario_input = menu.opciones()
aPagar = total(comidas_list)
print("\nEl Total a Pagar es: $",aPagar)






    