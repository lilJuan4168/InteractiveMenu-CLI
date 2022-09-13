from time import sleep
import json



class Comidas():
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.cantidad = 0
        self.precio = precio
    def aumentar_cant(self,x):
        self.cantidad += x
    def modificar_precio(self,y):
        self.precio = y


class Menu():
    def __init__(self,titulo,lista):
        self.titulo = titulo
        self.subttitulo = "Menu\n"
        self.lista = lista
    
    def despliegue(self):
        print("\n$---"+self.titulo.title()+"---$\n\n")
        print(self.subttitulo)
        for item in self.lista:
            i = self.lista.index(item) + 1
            print(str(i)+"----"+item.nombre.title()+" $",item.precio,"\n")
            sleep(0.2)
    
    def carrito(self):
        print("Carrito---> ",end="")
        for item in self.lista:
            print(item.nombre.title()+":",item.cantidad, end= " ")
        print("")

    def user_input(self):
        opcion = input("Elige una Opcion o Presione una LETRA para Enviar: ")
        try:
            g = int(opcion)
            for items in self.lista:   
                if g == 1234:
                    return (bool(True), bool(True))     
                elif g == int(self.lista.index(items)) + 1:
                    try: 
                       cantidad = int(input("Cuantas Unidades?: "))
                       return (int(opcion), int(cantidad))
                    except:
                        print("Solo Numeros!")
                        sleep(5)
                        return (99,99)
                elif g > len(self.lista):
                    print("Opcion Fuera de Rango Elegir Entre 1 y",len(self.lista))
                    sleep(5)
                    return(99,99)      
        except:
            return (bool(False),bool(False))

                
    def seleccion(self,opcion,cantidad):       
        self.lista[opcion - 1].aumentar_cant(cantidad)

    def restart(self):
        for items in self.lista:
            items.cantidad = 0
    
    def suma(self):
        resultado = 0
        for items in self.lista:
            resultado += items.cantidad * items.precio
        mensaje = "el total a pagar es de $"+str(resultado)
        return print(mensaje.title())
    
def leer_data(file):
    with open(file,"r") as c:
        datos = json.load(c)
        return datos

def list_of_obj(lista_de_diccionarios):
    x = []
    for items in lista_de_diccionarios:
        n = items["nombre"]
        p = items["precio"]
        nom = Comidas(n,p)
        x.append(nom)
    return x

def cargar_data(diccionario,lista_de_diccionarios,file):
    lista_de_diccionarios.append(diccionario)
    with open(file,"w") as c:
        json.dump(lista_de_diccionarios,c,indent=0)
    msg = "Carga Completa"
    return print(msg)


    







