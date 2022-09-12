from objetos import*
from time import sleep

def agregar_comida():
    print("///Menu Agregar Comida")
    sleep(1)
    nombre = input("Escribir el nombre:")
    cantidad = int(input("Escribir cantidad:"))
    precio = int(input("Escribir precio:"))
    nombre = Comida(nombre,cantidad,precio)
    return nombre
    
def total(lista):
    resultado = 0
    for items in lista:
        resultado += items.cantidad * items.precio
    return resultado

#def guardando_pedido():

def restart(x):
    for items in x:
        x.cantidad = 0

