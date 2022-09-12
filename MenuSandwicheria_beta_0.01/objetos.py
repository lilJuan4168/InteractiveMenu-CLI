from time import sleep 
from os import system

class Comida():
    def __init__(self,nombre,cantidad,precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    def aumentar_cantidad(self,cantidad=0):
        self.cantidad += cantidad
    def modificar_precio(self,x):
        self.precio += x

    
class Menu():
    def __init__(self,y):
        self.titulo = "\n****Bienvenidos a la Sandwicheria****\n\n"
        self.subtitulo = "Menu\n"
        self.comidas = y
        self.seguir = True
    def listar_menu(self):
        print(self.titulo)
        sleep(0.5)
        print(self.subtitulo)
        for c in self.comidas: 
            i = self.comidas.index(c) + 1
            print(i,"---",c.nombre," $",c.precio)
            sleep(0.5)
        print("")
    def opciones(self):    
        while self.seguir:
            print("Carrito -----> ",end="")
            for x in self.comidas:
                print(x.nombre+":",str(x.cantidad),end = "  ")
            try:
               x = int(input("\n\nElegir una OPCION o Presione una LETRA para Enviar:")) 
               z = int(input("Cuantas Unidades Desea?:")) 
            except:
               self.seguir = False
               break    
            self.comidas[x-1].aumentar_cantidad(z) #esto aumenta las cantidades
            system("clear")
            for c in self.comidas: 
               i = self.comidas.index(c) + 1
               print(i,"---",c.nombre," $",c.precio)
               sleep(0.3)
               print("")    
           

                  
                

            
           


            
            

           


        


                
        

    











  

