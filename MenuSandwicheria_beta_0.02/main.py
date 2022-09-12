from objetos import *
from time import sleep
from os import system
from comidas import *

titulo =  "bienvenidos a la sandwicheria"
loop = True
menu = Menu(titulo,food)

while loop:
    menu.despliegue()
    menu.carrito()
    u = menu.user_input()
   
    if u == (True,True):
       menu.crear_poo()
    elif u == (False,False):
        menu.suma()
        sleep(5)
        loop = False
    elif u == (99,99):
        system("clear")
        break
    else:
        menu.seleccion(u[0],u[1])
    system("clear")





