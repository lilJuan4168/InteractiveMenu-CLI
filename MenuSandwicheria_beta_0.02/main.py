from objetos import *
from time import sleep
from os import system

titulo =  "bienvenidos a la sandwicheria"
file = "comidas.json"
file_data = leer_data(file)
food = list_of_obj(file_data)  
menu = Menu(titulo,food)
loop = True

while loop:
   
    menu.despliegue()
    menu.carrito()
    u = menu.user_input()
   
    if u == (True,True):
       system("clear")
       nombre = input("Escribir nombre de nuevo elemento: ")
       precio = int(input("Escribir precio de nuevo elemento: "))
       new_dic = {"nombre":nombre,"precio":precio}
       cargar_data(new_dic,file_data,file)
       sleep(4)
       break
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





